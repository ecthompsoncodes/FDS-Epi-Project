# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:48:46 2024

@author: scott
"""
import os as os

fileloc = "C:\\Users\\scott\\OneDrive\\Documents\\FDS 510\\Dataset"
os.chdir(fileloc)

# Dataset loading
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading in county and census data and sorting for NC
county_data = pd.read_csv("us-counties-2021.csv")

# Prepping census data to be merged
white = pd.read_csv("census_data.csv")
white2 = white[['county', 'pct_white']]

del white

white2['pct_white'] = 1 - white2['pct_white']
white2 = white2.rename(columns = {'pct_white': 'Minority_pct'})
white2['Minority_pct'] = round(white2['Minority_pct'], 4)


census = pd.read_csv("County_totals2022.csv")
census = census.drop(census.columns[[1, 2, 4]], axis = 1)
census.columns.values[1] = 'Population'
census.columns.values[0] = 'county'
census = census.drop(census.index[-1])

#Sorting the data by State
nc_cd = county_data.query('state == "North Carolina"')

del county_data

#Merging the two datasets together and setting date formats
nc_cd = pd.merge(nc_cd, census, on = 'county', how = 'left')

nc_cd['Population'] = pd.to_numeric(nc_cd['Population'].str.replace(',', ''), errors='coerce')

nc_cd['date'] = pd.to_datetime(nc_cd['date'], format = '%Y-%m-%d')

# Date range
start_date = '2021-07-01'
end_date = '2021-12-02'

nc_cd = nc_cd[(nc_cd['date'] >= start_date) & (nc_cd['date'] <= end_date)]

# Cases and death proportion variables
nc_cd['casesprop'] = round(nc_cd['cases']/nc_cd['Population'], 4)
nc_cd['deathsprop'] = round(nc_cd['deaths']/nc_cd['Population'], 4)

# Daily and weekly for cases and deaths
nc_cd['dailycase'] = nc_cd.groupby('county')['cases'].diff().fillna(0)

nc_cd['weeklycase'] = nc_cd.groupby('county')['cases'].diff(periods=7).fillna(0)

nc_cd['dailydeath'] = nc_cd.groupby('county')['deaths'].diff().fillna(0)

nc_cd['weeklydeath'] = nc_cd.groupby('county')['deaths'].diff(periods=7).fillna(0)

nc_cd['weeklyper100k'] = round(nc_cd['weeklycase']/(nc_cd['Population']/100000), 2)

def transmission_level(weeklyper100k):
        if 0 <= weeklyper100k < 10:
            return 'Low'
        elif 10 <= weeklyper100k < 50:
            return 'Moderate'
        elif 50 <= weeklyper100k < 100:
            return 'Substantial'
        elif 100 <= weeklyper100k:
            return 'High'
        else:
            return 'Error'
        
nc_cd['tranlevel'] = nc_cd['weeklyper100k'].apply(transmission_level)


nc_cd = pd.merge(nc_cd, white2, on = 'county', how = 'left')
 
nc_cd2 = nc_cd.drop(nc_cd[nc_cd['tranlevel'] == 'Error'].index)


# Sorting the counties by region for base visualizations
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

# Assign regions to create a region dataset
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

nc_cd2['region'] = nc_cd2['county'].apply(assign_region)
print(nc_cd2['region'].value_counts())

nc_cd2.to_csv('countyall.csv')

region_df = nc_cd2.groupby(['region', 'date']).agg({'cases': 'sum', 'deaths': 'sum', 'dailycase': 'sum',
                                                   'weeklycase': 'sum', 'dailydeath': 'sum', 'weeklydeath':
                                                       'sum'}).reset_index()
region_df = region_df.sort_values(by = 'date')


sns.lineplot(x='date', y='deaths', hue='region', data=region_df)

plt.show()

sns.lineplot(x='date', y='cases', hue='region', data=region_df)

plt.show()

sns.lineplot(x='date', y='dailydeath', hue='region', data=region_df)

plt.show()

sns.lineplot(x='date', y='weeklydeath', hue='region', data=region_df)

plt.show()

sns.lineplot(x='date', y='weeklydeath', hue='region', data=region_df)

plt.show()

