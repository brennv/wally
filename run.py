from ops import docs
from scout import Scout
# from apscheduler.scheduler import Scheduler


def main():
    for i in docs:
        print(i)
        runner = Scout(i)
        runner.go()


if __name__ == '__main__':
    main()
