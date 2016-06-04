from ops import get_docs
from scout import Scout
import os
# from apscheduler.scheduler import Scheduler


env = 'dev'

def main(env):
    configs = './domains'
    if env == 'dev':
        configs = os.getenv('DOMAINS') or './domains'
    docs = get_docs(configs)
    for doc in docs:
        scout = Scout(domain)
        scout.run()

if __name__ == '__main__':
    main(env)
