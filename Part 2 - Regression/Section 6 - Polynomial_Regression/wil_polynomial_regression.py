#!/usr/bin/env python

# File information
"""
wil_polynomial_regression.py: First look at polynomial regression of data.
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


# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
print(dataset.head)
# Upper bound of range is always ignored, but need as a matrix, so include 1:2
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

plot = plt.scatter(X, y, color = "red")
plt.show(plot)

# Fit the linear model
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X, y)

print(linreg)

# Polyomial
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)

# Fit the model
linreg2 = LinearRegression()
linreg2.fit(X_poly,y)

# plot
plt.scatter(X,y,color = 'red')
plt.plot(X,linreg.predict(X), color = 'blue')
plt.title('What')
plt.xlabel('Real')
plt.ylabel('Model')
plt.show()

# plot the polynomial
X_grid = np.arange(min(X),max(X),0.1) # For a smoother curve
X_grid = X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color = 'red')
plt.plot(X_grid,linreg2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('What')
plt.xlabel('Real')
plt.ylabel('Model')
plt.show()

# Predict using the linear model
linreg.predict(6.5)

# Predict using the polynomial
linreg2.predict(poly_reg.fit_transform(6.5))
