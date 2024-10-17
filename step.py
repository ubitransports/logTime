import re
from math import trunc

import numpy as np
from colorama import Fore, Style

import repeatingstep


class Step:
    def __init__(self, name, start, end, sub_types=None):
        if sub_types is None:
            sub_types = list()
        self.name = name
        self.isSubtype = False
        self.startPattern = re.compile(start)
        self.endPattern = re.compile(end)
        self.sub_steps = sub_types
        for sub_type in self.sub_steps:
            sub_type.isSubtype = True
        self.start = 0
        self.end = 0
        self.duration = 0
        self.occurrences = []

    def reset(self):
        self.start = 0
        self.end = 0
        self.duration = 0
        for sub_step in self.sub_steps:
            if isinstance(sub_step, repeatingstep.RepeatingStep):
                sub_step.end_repeating()

    def terminate(self):
        pass

    def search(self, _line, _time):
        found = self.startPattern.search(_line)
        if found is not None:
            # Found step start
            self.start = _time
        elif self.start != 0:
            found = self.endPattern.search(_line)
            if found is not None:
                # Found step end
                self.end = _time
                self.duration = (self.end - self.start).total_seconds() * 1000
                self.occurrences.append(self.duration)
                self.reset()
            else:
                # Sub step
                if self.sub_steps:
                    for sub_step in self.sub_steps:
                        sub_step.search(_line, _time)

    def print(self, level=0):
        _data = np.array(self.occurrences)
        tabs = level*"\t"
        self.print_decorate()
        print(f"{tabs}The total number of operation for {Fore.BLUE}'{self.name}'{Style.RESET_ALL}: {_data.size:d}")
        if _data.size > 0:
            print("{}MIN: {:.0f}ms".format(tabs, _data.min()))
            print("{}MAX: {:.0f}ms".format(tabs, _data.max()))
            print("{}MEDIAN: {:.0f}ms".format(tabs, np.median(_data)))
            print("{}ST DEVIATION: {:.0f}ms".format(tabs, np.std(_data)))
            print(Fore.GREEN + "{}MEAN: {:.0f}ms".format(tabs, np.mean(_data)) + Style.RESET_ALL)
            for sub_step in self.sub_steps:
                sub_step.print(level + 1)
        self.print_decorate()

    def print_decorate(self):
        print("===========================================================================================")

    def __str__(self):
        return "Step start: {} end: {} duration: {:d} ms".format(self.start, self.end, trunc(self.duration))

    def export(self, writer):
        _data = np.array(self.occurrences)
        if _data.size > 0:
            if not self.isSubtype:
                writer.writerow([self.name, "", _data.min(), _data.max(), np.median(_data), np.mean(_data), np.std(_data)])
            else:
                writer.writerow(
                    ["", self.name, _data.min(), _data.max(), np.median(_data), np.mean(_data), np.std(_data)])
            for sub_step in self.sub_steps:
                sub_step.export(writer)
