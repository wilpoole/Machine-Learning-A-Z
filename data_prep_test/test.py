import pandas as pd
import numpy as np

from dataprep import data_load

from os import path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Variables
data_directory = "../Part 1 - Data Preprocessing/data"
data_file = "data.csv"

# Load test data
df = data_load.data_load(data_directory, data_file)

df = data_preparation(df, process_missing_values = True)
