#!/usr/bin/env python

# File information
"""
wil_regression.py: First look at regression of data.
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
data_file = "Salary_Data.csv"


# Import the data
data_set = pd.read_csv(path.join(data_directory, data_file))


# Split the data into training and testing
data_set_train, data_set_test = train_test_split(
  data_set.values , test_size = 0.333, random_state = 0
  )


# Fitting a linear model to the data
regressor = LinearRegression()
model = regressor.fit(data_set_train[:, 0].reshape(-1, 1),
  data_set_train[:, 1].reshape(-1, 1))

# Fit the model to the test dataset
data_set_predict = regressor.predict(data_set_test[:, 0].reshape(-1, 1))


plot = plt.scatter(data_set_train[:,0], data_set_train[:,1], color = "red")
plot = plt.scatter(data_set_test[:,0], data_set_test[:,1], color = "green")
plot = plt.plot(
  data_set_train[:,0],
  regressor.predict(data_set_train[:,0].reshape(-1, 1)),
  color = "blue")
plot = plt.title("Salary vs Experience")
plot = plt.xlabel("Experience (Yrs)")
plot = plt.ylabel("Salary ($)")
plt.show(plot)
