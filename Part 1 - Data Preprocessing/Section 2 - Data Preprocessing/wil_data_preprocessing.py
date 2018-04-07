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

from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Variables
data_directory = "data"
data_file = "data.csv"

# Models
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)

# Data import
data_set = pd.read_csv(path.join(data_directory, data_file))

# Data format
data_set_dependent = data_set.iloc[ : , :-1 ].values
data_set_independent = data_set.iloc[ : , -1 ].values

data_set_dependent = imputer.fit_transform(data_set_dependent[ : , 1:3 ])

data_set_dependent[:, 0] = LabelEncoder().fit_transform(
  data_set_dependent[:, 0]
  )

data_set_dependent = OneHotEncoder(
  categorical_features = [0]
  ).fit_transform(data_set_dependent).toarray()
len(data_set_dependent)

data_set_independent = LabelEncoder().fit_transform(data_set_independent)
print(data_set_independent)

data_set_dependent_train, data_set_dependent_test, data_set_independent_train, data_set_independent_test = train_test_split(
  data_set_dependent, data_set_independent, test_size = 0.2, random_state = 0
  )

dependent_scaler = StandardScaler()
data_set_dependent_train = dependent_scaler.fit_transform(data_set_dependent_train)
data_set_dependent_test = dependent_scaler.transform(data_set_dependent_test)
