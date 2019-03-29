from typing import List, Tuple

import pandas as pd

from glob import glob
from os import path

TaggedName = Tuple[str, pd.DataFrame]
TaggedNameList = List[TaggedName]

def get_testing_set(folder: str, prefix: str) -> TaggedNameList:
    """I've laid out my testing data so that each set of files starts with the same prefix. This
        function takes a reference to the folder test data resides in and the prefix that's
        currently of interest and it returns a list of tuples containing the data names and the
        actual data

        :param folder: The location where you're keeping the test data
        :param prefix: The prefix (separated from file name by an underscore) associated with
            the set of datasets you're interested in
        :return: A list of tuples, where the first item of each is the data's name and the second
            item the actual data, as a pandas dataframe.
    """
    gpath = path.join(folder, prefix)
    gpath += '_*'
    files = glob(gpath)

    return [(f_path.split(f'{prefix}_')[-1].split('.')[0], pd.read_csv(f_path, sep='\t', header=None))
            for f_path in files]