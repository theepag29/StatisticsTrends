# -*- coding: utf-8 -*-

# Student ID:   2231457
# Name:         Theepag Atputhalingam

import pandas as pd
# import matplotlib.pyplot as plt

def read_world_bank_data(filename, countries, years):
    """
    Function to read the csv file and return 2 dataframes,one with years 
    as columns and the other with countries as columns. Takes the filename as
    the parameter.
    """
    # read file into a dataframe
    df0 = pd.read_csv(filename, skiprows=4, index_col=0)
    print(df0.head(10))
    # some cleaning
    df0.drop(columns=["Country Code"], axis=1, inplace=True)
    df1 = df0.loc[countries,years]
    # dataframe methods for the points
    df1 = df1.sort_index().rename_axis("Years", axis=1)
    # transpose
    df2 = df1.T
    
    print(df1.head(10))
    # print(df2)
    
    return df1, df2

cntrs = ["Japan", "Russian Federation", "China", "Korea, Rep.", "Saudi Arabia", "United Kingdom", "Brazil",
                    "India", "United States", "Germany", "Canada"]
yrs = ["1990", "1995", "2000", "2005", "2010", "2015"]
df1, df2  = read_world_bank_data('C:/Users/ta22ado/OneDrive - University of Hertfordshire/Applied Data Science/Statistics Assignement/API_19_DS2_en_csv_v2_5346672.csv',
                                 cntrs, yrs)

     