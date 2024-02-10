import csv
import requests, re
from bs4 import BeautifulSoup
from pprint import pprint
import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import pandas as pd

import seaborn as sns
import plotly
import pandas as pd
import numpy as np
import plotly
import plotly.graph_objs as go
import plotly.express as px

def fuel_data_parser():
    df_fuel = pd.read_csv("2022_NTD_Annual_Data_-_Fuel_and_Energy_20231027.csv")
    df_fuel = df_fuel.fillna(0)
    df_fuel = df_fuel.drop(['NTD ID','Organization Type','Reporter Type','UACE Code','UZA Name',"Mode",'TOS','Gasoline Questionable'], axis = 1)
    # df = df[['Agency','City','State','Organization Type','Primary UZA Population','Agency VOMS',]]
    sum_columns = ["Diesel (gal)", "Diesel (gal) Questionable", "Gasoline (gal)", "Gasoline (gal) Questionable", "Liquefied Petroleum Gas (gal equivalent)", "Liquefied Petroleum Gas (gal equivalent) Questionable", "Compressed Natural Gas (gal equivalent)", "Compressed Natural Gas (gal equivalent) Questionable", "Bio-Diesel (gal)", "Bio-Diesel (gal) Questionable", "Other Fuel (gal/gal equivalent)", "Other Fuel (gal/gal equivalent) Questionable", "Electric Propulsion (kWh)", "Electric Propulsion (kWh) Questionable", "Electric Battery (kWh)", "Electric Battery (kWh) Questionable"
]
    df_fuel1 = df_fuel.groupby(by= 'Agency')[sum_columns].sum()
    pprint(df_fuel1.head())
    pprint(len(df_fuel1))

    pprint(df_fuel.dtypes)
    df_fuel1.to_csv("cleaned_fuel.csv")
fuel_data_parser()