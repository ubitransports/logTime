import numpy as np
from colorama import Fore, Style

from step import Step


class RepeatingStep(Step):
    def __init__(self, name, start, end, sub_types=None):
        super().__init__(name, start, end, sub_types)
        self.total_times = []
        self.last_end_index = 0

    def end_repeating(self):
        self.total_times.append(sum(self.occurrences[self.last_end_index:]))
        self.last_end_index = len(self.occurrences)

    def print(self, level=0):
        super().print(level)
        _data = np.array(self.total_times)
        print(Fore.GREEN + "{}Total MEAN: {:.0f}ms".format(level*"\t", np.mean(_data)) + Style.RESET_ALL)

    def print_decorate(self):
        pass
