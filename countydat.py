# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:48:46 2024

@author: scott
"""
import os as os

os.chdir("C:\\Users\\scott\\OneDrive\\Documents\\FDS 510\\Dataset")

# Dataset loading
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

county_data = pd.read_csv("us-counties-2021.csv")

nc_cd = county_data.query('state == "North Carolina"')

del county_data

nc_cd['date'] = pd.to_datetime(nc_cd['date'], format = '%Y-%m-%d')

start_date = '2021-07-01'
end_date = '2021-12-01'

nc_cd = nc_cd[(nc_cd['date'] >= start_date) & (nc_cd['date'] <= end_date)]

Central_reg = ['Anson', 'Cabarrus', 'Gaston', 'Lincoln', 'Mecklenburg', 'Stanly', 'Union']

Coastal_reg = ['Beaufort', 'Bertie', 'Bladen', 'Brunswick', 'Camden', 'Carteret', 'Chowan',
               'Columbus', 'Craven', 'Currituck', 'Dare', 'Duplin', 'Edgecombe', 'Gates',
               'Greene', 'Halifax', 'Hertford', 'Hyde', 'Johnston', 'Jones', 'Lenoir',
               'Martin', 'Nash', 'New Hanover', 'Onslow', 'Pamlico', 'Pasquotank', 'Pender',
               'Perquimans', 'Pitt', 'Robeson', 'Sampson', 'Tyrrell', 'Washington', 'Wayne',
               'Wilson']

Eastern_reg = ['Caswell', 'Chatham', 'Cumberland', 'Durham', 'Franklin', 'Granville',
               'Harnett', 'Hoke', 'Lee', 'Montgomery', 'Moore', 'Northampton', 'Orange',
               'Person', 'Richmond', 'Scotland', 'Vance', 'Wake', 'Warren']

Northern_reg = ['Alamance', 'Alexander', 'Alleghany', 'Ashe', 'Caldwell', 'Catawba',
                'Davidson', 'Davie', 'Forsyth', 'Guilford', 'Iredell', 'Randolph',
                'Rockingham', 'Rowan', 'Stokes', 'Surry', 'Yadkin', 'Watauga', 'Wilkes']

Western_reg = ['Avery', 'Buncombe', 'Burke', 'Cherokee', 'Clay', 'Cleveland', 'Graham',
               'Haywood', 'Henderson', 'Jackson', 'Macon', 'Madison', 'McDowell', 'Mitchell',
               'Polk', 'Rutherford', 'Swain', 'Transylvania', 'Yancey']

def assign_region(county):
    if county in Central_reg:
        return 'Central'
    elif county in Coastal_reg:
        return 'Coastal'
    elif county in Eastern_reg:
        return 'Eastern'
    elif county in Northern_reg:
        return 'Northern'
    elif county in Western_reg:
        return 'Western'
    else:
        return 'Error'

nc_cd['region'] = nc_cd['county'].apply(assign_region)
print(nc_cd['region'].value_counts())

region_df = nc_cd.groupby(['region', 'date']).agg({'cases': 'sum', 'deaths': 'sum'}).reset_index()
region_df = region_df.sort_values(by = 'date')


sns.lineplot(x='date', y='deaths', hue='region', data=region_df)

plt.show()


sns.lineplot(x='date', y='cases', hue='region', data=region_df)

plt.show()




