"""Tool for generating graphs of each dataset in a collection."""

import argparse
import atexit

import seaborn as sns  # I'm vain

from matplotlib import pyplot as pp

from Tools.tsv_handler import get_testing_set

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('folder', type=str, help='the folder where data resides')
parser.add_argument('prefix', type=str, help='the prefix, absent any underscores, that identifies '
                                             'files in the desired set')


if __name__ == '__main__':
    args = parser.parse_args()
    folder = args.folder
    prefix = args.prefix

    datasets = get_testing_set(folder, prefix)

    sns.set()  # make my graphs pretty, seaborn!
    figures = []

    # Make sure we properly clean-up the memory from our figures
    def kill_figures():
        for figure in figures:
            pp.close(figure)
    atexit.register(kill_figures)

    for ds in datasets:
        title, data = ds
        fig = pp.figure()
        ax = fig.subplots()
        ax.plot(data[0], data[1], 'k.')
        ax.set_title(title)
        figures.append(fig)

    pp.show()

