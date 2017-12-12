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

def expand_categorical_features(df, dependent):
    """ Expand independent categorical features to individual columns """

    # Find categorical columns
    df_categorical = pd.Series(
        [df[c].value_counts().index[0]
        if df[c].dtype == np.dtype('O')
        for c in df],
        index=df.columns)
    df_categorical = df.fillna(df_fill)


    data_set_dependent[:, 0] = LabelEncoder().fit_transform(
      data_set_dependent[:, 0]
      )

    data_set_dependent = OneHotEncoder(
      categorical_features = [0]
      ).fit_transform(data_set_dependent).toarray()

    data_set_independent = LabelEncoder().fit_transform(data_set_independent)
