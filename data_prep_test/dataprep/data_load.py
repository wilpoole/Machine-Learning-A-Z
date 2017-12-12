#!/usr/bin/env python

# File information
"""
data_load.py: Loads csv file given the data directory and file name.
"""
__author__ = "Wil Poole"
__copyright__ = "2017"
__credits__ = "Wil Poole"
__license__ = "None"
__version__ = "0.1"
__maintainer__ = "Wil Poole"
__email__ = "@"
__status__ = "Development"

def data_load(data_directory, data_file):
    # Load the data
    print("Loading data...")
    df = pandas.read_csv(path.join(data_directory, data_file))
    print("...data loaded.")
    return df
