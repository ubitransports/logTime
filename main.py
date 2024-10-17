import argparse
import re
import sys
import csv
from datetime import datetime
from pathlib import Path

from steps import STEPS_LIST

try:
    import numpy as np
    from colorama import init as colorama_init
    from colorama import Fore
    from colorama import Style
except ImportError as error:
    print("You don't have module {0} installed".format(error.msg[16:]))
    sys.exit(-1)

# TOTOOLS_LINE = re.compile(r"^(?P<datetime>\d\d-\d\d-\d\d \d\d:\d\d:\d\d.\d{3})\s*(?P<PID>\d*)\s*(?P<level>\w+)\s*(?P<module>.*?)\s*(?P<log>.*)$")
#TOTOOLS_LINE = re.compile(r"^(?P<datetime>\d\d-\d\d-\d\d \d\d:\d\d:\d\d.\d{3})\s*(?P<PID>\d*)\s*(?P<TID>\d*)\s*(?P<level>\w+)\s*(?P<module>.*?)\s*(?P<log>.*)$")
TOTOOLS_LINE = re.compile(r"^(?P<datetime>\d\d-\d\d \d\d:\d\d:\d\d.\d{3})\s*(?P<PID>\d*)\s*(?P<TID>\d*)\s*(?P<level>\w+)\s*(?P<module>.*?)\s*(?P<log>.*)$")
PERF_APP_LINE = re.compile(r"^(?P<datetime>\d\d-\d\d \d\d:\d\d:\d\d.\d{3})\s*(?P<TID>\[.*?\])\s*(?P<level>\w+)\s*(?P<module>.*?)\s(?P<log>.*)$")
FORMATS = [TOTOOLS_LINE, PERF_APP_LINE]


def timestamp_to_time(timestamp):
    return datetime.strptime(timestamp, "%m-%d %H:%M:%S.%f")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='logTime',
        description='Parse logs and print out operation measures.')
    parser.add_argument('filepath')
    parser.add_argument('--list', dest='list', help='List available step lists', action='store_true')
    parser.add_argument("--steps", dest="steps", choices=STEPS_LIST.keys(), default=list(STEPS_LIST.keys())[0])
    parser.add_argument("--export", dest="export", help="Export to CSV file", action='store_true')
    args = parser.parse_args()

    if args.list:
        print("Available step lists: " + str(list(STEPS_LIST.keys())))
        sys.exit(0)

    STEPS = STEPS_LIST[args.steps]

    colorama_init()
    opened_file = open(args.filepath)

    match = None
    for line in opened_file.readlines():
        for f in FORMATS:
            match = f.search(line)
            if match is None:
                continue

        if match is None:
            print("Line not matched" + str(line))
            continue

        data = match.groupdict()
        time = datetime.strptime(data["datetime"], "%m-%d %H:%M:%S.%f")

        for step in STEPS:
            step.search(line, time)

    opened_file.close()

    if not args.export:
        print("===========================================================================================")
        print(f"\t\t\tReport for {Fore.RED}{Style.BRIGHT}{Path(args.filepath).stem.upper()}{Style.RESET_ALL}")
        for step in STEPS:
            step.print()
    else:
        with open(f"{Path(args.filepath).stem.upper()}.csv", 'w') as file:
            writer = csv.writer(file)
            fields = ["Step", "Sub step", "Min", "Max", "Median", "Mean", "Standard deviation"]
            writer.writerow(fields)
            for step in STEPS:
                step.export(writer)
        print(f"Result exported to CSV file {Fore.RED}{Style.BRIGHT}{file.name}{Style.RESET_ALL}")

