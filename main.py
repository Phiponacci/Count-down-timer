import time
import datetime


def countdown(hours, mins, secs):
    total_secs = hours * 60 * 60 + mins * 60 + secs
    for remaining in range(total_secs, -1, -1):
        _time = datetime.timedelta(seconds=remaining)
        print("\r", _time, end='')
        time.sleep(1)

    print("\nTime's up")


if __name__ == '__main__':
    hours = int(input('hours: '))
    mins = int(input('minutes: '))
    secs = int(input('seconds: '))
    countdown(hours, mins, secs)
