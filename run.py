from controller import apis
from scout import Scout


def main():
    for api in apis:
        scout = Scout(api)
        scout.run()

if __name__ == '__main__':
    main()
