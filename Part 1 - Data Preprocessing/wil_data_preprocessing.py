#!/usr/bin/env python

# File information
"""
wil_data_preprocessing.py: First look at preprocessing data.
"""
__author__ = "Wil Poole"
__copyright__ = "2017"
__credits__ = "Wil Poole"
__license__ = "None"
__version__ = "0.1"
__maintainer__ = "Wil Poole"
__email__ = "@"
__status__ = "Development"



# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from os import path
from sklearn.preprocessing import Imputer

# Variables
data_directory = "data"
data_file = "data.csv"




# Data import
data_set = pd.read_csv(path.join(data_directory, data_file))


# Data format
data_set_dependent = data_set.iloc[ : , :-1 ].values
data_set_independent = data_set.iloc[ : , -1 ].values
