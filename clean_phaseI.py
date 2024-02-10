import csv
import requests, re
from pprint import pprint
import seaborn as sns
import pandas as pd
import numpy as np


def fuel_data_parser():
    df_fuel = pd.read_csv("2022_NTD_Annual_Data_-_Fuel_and_Energy_20231027.csv")
    df_fuel = df_fuel.fillna(0)
    df_fuel = df_fuel.drop(['NTD ID','Organization Type','Reporter Type','UACE Code','UZA Name',"Mode",'TOS',
    'Gasoline Questionable'], axis = 1)
    # df = df[['Agency','City','State','Organization Type','Primary UZA Population','Agency VOMS',]]
    sum_columns = ["Mode VOMS", "Diesel (gal)", "Gasoline (gal)", "Liquefied Petroleum Gas (gal equivalent)", 
     "Compressed Natural Gas (gal equivalent)",  "Other Fuel (gal/gal equivalent)",  "Electric Propulsion (kWh)", 
      "Electric Battery (kWh)"]
    df_fuel1 = df_fuel.groupby(by= 'Agency')[sum_columns].sum()
    pprint(df_fuel1.head())
    pprint(len(df_fuel1))
    df_fuel1.to_csv("cleaned_fuel.csv")
fuel_data_parser()


