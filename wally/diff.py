from sqlalchemy import create_engine
from tqdm import tqdm
import pandas as pd


def get_df(domain):
    '''Combine dataset metadatas into a dataframe.'''
    print('Checking domain...', domain)
    uids = get_keys(domain)
    # uids = uids[0:4]  # testing
    names, times, rowCounts, columnCounts, columnNames, blurbs = [], [], [], [], [], []
    for uid in tqdm(uids):
        name, updated, rowCount, columnCount, columns, blurb = get_metadata(domain, uid)
        names.append(name)
        times.append(updated)
        rowCounts.append(rowCount)
        columnCounts.append(columnCount)
        columnNames.append(columns)
        blurbs.append(blurb)
    df = pd.DataFrame()
    df['uid'] = uids
    df['name'] = names
    df['blurb'] = blurbs
    df['time'] = times
    df['rowCount'] = [x for x in rowCounts]
    df['columnCount'] = [x for x in columnCounts]
    df['columns'] = [str(x) for x in columnNames]
    # df = df.set_value(0, 'rowCount', 1240)  # testing
    df = df.set_index('uid').sort_index()
    return df

def set_db(db_uri, db_table, df):
    '''Save dataframe as database table.'''
    print('Setting db...', db_uri, db_table)
    engine = create_engine(db_uri)
    with engine.connect() as conn, conn.begin():
        df.to_sql(db_table, conn, if_exists='replace')
    return True

def get_db(db_uri, db_table):
    '''Read sqlite table into dataframe.'''
    print('Getting db...', db_uri, db_table)
    engine = create_engine(db_uri)
    with engine.connect() as conn, conn.begin():
        df1 = pd.read_sql_table(db_table, conn)
        df1 = df1.set_index('uid').sort_index()
    return df1

def check_diff(db_uri, db_table, domain):
    '''Check if stored data is up to date, return dataframes.'''
    print('Checking diff...')
    df1, df2 = get_db(db_uri, db_table), get_df(domain)
    is_different = True
    if df2.equals(df1):
        is_diff = False
    return df1, df2, is_different

def diff_rows(df1, df2):
    '''Diff dataframe rows & find common keys.'''
    df_new, df_old = pd.DataFrame(), pd.DataFrame()
    index1, index2 = list(df1.index), list(df2.index)
    key_additions = [x for x in index2 if x not in index1]
    if key_additions:
        df_new = df2.loc[df2.index.isin(key_additions)]
    key_deletions = [x for x in index1 if x not in index2]
    if key_deletions:
        df_old = df1.loc[df1.index.isin(key_deletions)]
    common_keys = [x for x in index2 if x in index1]
    return df_new, df_old, common_keys

def diff_cells(df1, df2, common_keys):
    '''Diff the columnCounts.'''
    if common_keys:
        df1 = df1.loc[df1.index.isin(common_keys)]
        df2 = df2.loc[df2.index.isin(common_keys)]
        df1_num = df1._get_numeric_data()
        df2_num = df2._get_numeric_data()
        df_mod = df2_num.subtract(df1_num)
        df_mod = df_mod.drop('columnCount', axis=1)  # long shortcut
        df_mod = df_mod[(df_mod.T != 0).any()]
        df_mod['name'] = [df2[df2.index == x]['name'][0] for x in df_mod.index]
    return df_mod

def add_row_note(domain, df, intro):
    '''Write note for datasets that are added or deleted.'''
    notes = []
    if len(df) > 0:
        df['url'] = ['https://' + domain + '/resource/' + x for x in df.index]
        # df['name'] = [x[:60] + (x[60:] and '..') for x for x in df['name']]
        df['url_tag'] = ['<' + x + '|' + y + '>' for x, y in zip(df['url'], df['name'])]
        df['note'] = [intro + ' ' + x for x in df['url_tag']]
        df['blurb'] = [x[:160] + (x[160:] and '..') for x in df['blurb']]
        df['note'] = [x + ' _' + y + '_' if len(y) > 2 else x for x, y in zip(df['note'], df['blurb'])]
        for note in df['note']:
            notes.append(note)
    if notes:
        notes = ' \n'.join(notes)
    return notes

def down_sample(items, n):
    '''Randomly down sample long lists.'''
    items = [items[x] for x in sorted(random.sample(list(range(len(items))), n))]
    return items

def add_cell_note(domain, name, df, add_icon, sub_icon):
    '''Write note for diff cell results.'''
    notes = []
    if len(df) > 0:
        df['url'] = ['https://' + domain + '/resource/' + x for x in df.index]
        df['url_tag'] = ['<' + x + '|' + y + '>' for x, y in zip(df['url'], df['name'])]
        df['note'] = [x for x in df['url_tag']]
        df['note'] = [add_icon + x + ' added ' if y > 0 else sub_icon + x + ' deleted ' for x, y in zip(df['note'], df['rowCount'])]
        # df['note'] = [x + ' added ' if y > 0 else x + ' deleted ' for x, y in zip(df['note'], df['rowCount'])]
        df['note'] = [x + str(abs(y)) for x, y in zip(df['note'], df['rowCount'])]
        df['note'] = [x + ' rows' if abs(y) > 1 else x + ' row' for x, y in zip(df['note'], df['rowCount'])]
        df = df.sort_values(by='name')
        for note in df['note']:
            notes.append(note)
    if notes:
        print('len mod notes', len(notes))
        if len(notes) > 5:
            trim = len(notes) - 5
            notes = down_sample(notes, 5)  # TODO add ranking and slicing
            s = 's'
            if trim == 1:
                s = ''
            notes = notes + ['_..and ' + str(trim) + ' additional <https://' + domain + '|' + name + 'update' + s + '>_']
        notes = ' \n'.join(notes)
    return notes

def get_notes(domain, df1, df2):
    '''Diff metdata and write notes.'''
    print('Diffing metdata and write notes...')
    df_new, df_dep, common_keys = diff_rows(df1, df2)
    # df_mod = diff_cells(df1, df2, common_keys)
    new_notes = add_row_note(domain, df_new, ':gift: *New* dataset added:')
    dep_notes = add_row_note(domain, df_dep, ':boom: Dataset removed:')
    # mod_notes = add_cell_note(domain, df_mod, add_icon='*+* ', sub_icon='*-* ')
    slack_note = [x for x in [new_notes, dep_notes] if x]  # , mod_notes
    slack_note = ' \n'.join(slack_note)
    twitter_note = ''  # TODO integrate twitter for new_notes
    if new_notes:
        twitter_note = ' \n'.join(new_notes)
    return slack_note, twitter_note
