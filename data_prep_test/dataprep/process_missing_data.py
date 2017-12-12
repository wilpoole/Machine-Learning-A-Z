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

def process_missing_data(df):
    """ Looks to see if missing data should be processed, and if so, looks for
    missing data and fills it """

    # Check if there is missing data
    if df.columns[df.isnull().any()].empty:
        print("No missing values found")
    # If there is, the fill the NaNs
    else:
        print("Found missing values...")
        # Find how to fill those missing values
        df_fill = pd.Series(
            [df[c].value_counts().index[0]
            if df[c].dtype == np.dtype('O')
            else df[c].mean()
            for c in df],
            index=df.columns)
        df_filled = df.fillna(df_fill)
        print("...which have been filled")
    # Return the df
    return df
