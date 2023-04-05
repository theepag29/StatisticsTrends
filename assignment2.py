# -*- coding: utf-8 -*-

# Student ID:   2231457
# Name:         Theepag Atputhalingam

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as sts


# Function to read file and filtering


def read_file(data, country, years):
    ''' Function to read CSV files. country and years are used
    to get the list of countries and years to be read from whole data. This
    function uses filtering technique to take the required values such as
    dropping and retrieving values using iloc[]. Once filtering is done, the
    dataframes are transposed'''
    df = pd.read_csv(data, skiprows=4)
    df.drop(columns=['Country Code'], axis=1, inplace=True)
    df1 = df.iloc[country, years]
    df2 = df1.T
    return df1, df2


# Function to print the overview of the dataframe

def describe(data):
    '''This function is used to explore the data using statistical
    tools. Argument data is used to retrieve the data. .describe() method
    is used to explore the dataframe getting the overview and understanding the
    value distribution. .corr() method is used to check the pairwise
    correlation of columns'''
    print(data.describe())
    print(data.corr())
    return


# Function to print statistical insights.

def statistics(data):
    '''This function is used to calculate a particular value using statistical
    tools. Statistical tools such as Skewness and Kurtosis are being used here.
    Argument data is passed here.'''
    print("Skewness: ", sts.skew(data))
    print("Kurtosis: ", sts.kurtosis(data))
    return


def heat_clean(data, column, value, year, indi_cators):
    df = data.groupby(column, group_keys=True)
    df = df.get_group(value)
    df = df.reset_index()
    df.set_index('Indicator Name', inplace=True)
    df = df.loc[:, year]
    df = df.T
    df = df.loc[:, indi_cators]
    df = df.dropna(axis=1)
    return df


# Function to plot dataframe

def plot(data, kind, title, x, y):
    ''' Function to create plots. This function is used to give an insight of
    the dataframes. Arguments such as data, kind, title, x, y are used. data
    arguement is used to get the dataframe, kind argument is to specify which
    graph to be plotted. title, x, and y are used to label the coordinates on
    the graph'''
    data.plot(kind=kind)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(loc='upper right', bbox_to_anchor=(1.4, 1.0))
    plt.show()


def plot_heat_map(data, country):
    plt.figure(figsize=(10, 7))
    heatmap = sns.heatmap(data.corr(), annot=True, cmap="YlGnBu")
    heatmap.set_title(country)

# Specifying the country list by id


country_list = [13, 35, 66, 106, 29]
year = [43, 48, 53, 58, 63]


# Specifying country names saving it in country_names[] list.

country_names = ["Australia", "Canada", "Ecuador", "Indonesia", "Brazil"]


# Datasets called to the read_file(), specifying the country_list and year.

forest_cnty, forest_yr = read_file("forestland.csv",
                                   country_list, year)
poptot_cnty, poptot_yr = read_file("poptotal.csv",
                                   country_list, year)
agrlnd_cnty, agrlnd_yr = read_file("agriland.csv",
                                   country_list, year)
aralnd_cnty, aralnd_yr = read_file("arableland.csv",
                                   country_list, year)

# Specifying country names to the columns of the dataframes.

forest_yr.columns = country_names
poptot_yr.columns = country_names
agrlnd_yr.columns = country_names
aralnd_yr.columns = country_names

# The variable of dataframes called to describe().

describe(forest_yr)
describe(aralnd_yr)
describe(poptot_yr)
describe(agrlnd_yr)


# Particular value of a dataframe being called to statistics().

statistics(forest_yr)

# Plotting graphs for various dataframes using plot()

plot(agrlnd_yr, 'line', 'Agricultural Land (% of land area)',
     'Years', 'Percentage(%)')
plt.savefig("agri.png")

plot(aralnd_yr, 'bar', 'Arable Land (% of land area)', 'Years', 'Percentage(%)')
plt.savefig("arable.png")

plot(poptot_yr, 'line', 'CO2 emissions (metric tons per capita)',
     'Years', 'metric tons per capita')
plt.savefig("poputotal.png")

plot(forest_yr, 'bar', 'Forest Area (% of land area)', 'Years', 'Percentage(%)')
plt.savefig("forest.png")

#reading climate dataset file

data = pd.read_csv("climatedata.csv", skiprows=4)
x = ["Forest area (% of land area)", "Arable land (% of land area)",
     "Population, total", "Agricultural land (% of land area)",
     "Urban population (% of total population)",
     "CO2 emissions (metric tons per capita)"]

years = ["2000", "2005", "2010", "2015", "2020"]

#clean data before ploting heatmap

data_cleaned = heat_clean(data, 'Country Name', 'Ecuador', years, x)
plot_heat_map(data_cleaned, 'Ecuador')