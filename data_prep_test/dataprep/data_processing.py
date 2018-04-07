#!/usr/bin/env python

# File information
"""
data_processing.py: Process data ready for something
"""
__author__ = "Wil Poole"
__copyright__ = "2017"
__credits__ = "Wil Poole"
__license__ = "None"
__version__ = "0.1"
__maintainer__ = "Wil Poole"
__email__ = "@"
__status__ = "Development"

def data_preparation(df, dependent_column,
    process_missing_values = True, feature_scaling = True, encode = True
    ):
    """ Loads and processes data ready for analysis """

    # Look for missing values
    if process_missing_values:
        df = process_missing_data(df)

    # Categorical values
    if encode:
        df = expand_categorical_features(df, dependent_column)

    # Feature scaling
    if feature_scaling:
        df = scale_features(df)

    # Split into training and test set



    return df
