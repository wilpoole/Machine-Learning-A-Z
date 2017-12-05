#!/usr/bin/env python

# File information
"""
wil_multiple_linear_regression.py: First look at multiple regression of data.
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
import seaborn as sns

from os import path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Variables
data_directory = "."
data_file = "50_Startups.csv"
