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

# Import the data
data_set = pd.read_csv(path.join(data_directory, data_file))

# Print the data set
data_set.head(n=5)


# Split into dependent and independent data
X = data_set.iloc[:, :-1].values
y = data_set.iloc[:, 4].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
print(X[1:4,3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap - remove the first column
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

print(y_pred)
