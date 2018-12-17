'''
Helper functions to do EDA
'''

import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt


def categorical_summarized(dataframe, x=None, y=None, hue=None, palette='Set1'):
    '''
    Helper function that gives a quick summary of a given columns of categorical data

    Arguments
    =========
    dataframe: pandas dataframe
    x: str. horizontal axis to plot the labels of categorical data, y would be the count
    y: str. vertical axis to plot the labels of categorical data, x would be the count
    hue: str. if you want to compare it another variable (usually the target variable)
    palette: array-like. Colour of the plot

    Returns
    =======
    Quick Stats of the data and also the count plot
    '''
    if x == None:
        column_interested = y
    else:
        column_interested = x
    series = dataframe[column_interested]
    print(series.describe())
    print('mode: ', series.mode())
    print('='*80)
    print(series.value_counts())
    sns.countplot(x=x, y=y, hue=hue, data=dataframe, palette=palette)
    plt.show()


if __name__ == "__main__":
    pass
