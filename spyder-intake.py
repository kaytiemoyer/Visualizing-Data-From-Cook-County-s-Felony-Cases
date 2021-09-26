# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
%matplotlib inline
import seaborn as sns

df = pd.read_csv('C:/Users/Kaytie/Desktop/School/Regis University/Fall 2021/MSDS 670/Intake.csv')
to_drop = ['CASE_ID','CASE_PARTICIPANT_ID','RECEIVED_DATE','PARTICIPANT_STATUS','INCIDENT_CITY','INCIDENT_BEGIN_DATE','INCIDENT_END_DATE','LAW_ENFORCEMENT_UNIT','ARREST_DATE','FELONY_REVIEW_DATE']
df.drop(to_drop, inplace = True, axis = 1)
df.head(5)

new_name = {'OFFENSE_CATEGORY': 'Offense',
           'AGE_AT_INCIDENT': 'Age',
           'RACE': 'Race',
           'GENDER': 'Gender',
           'LAW_ENFORCEMENT_AGENCY': 'Agency',
           'FELONY_REVIEW_RESULT': 'Review Result',
           'UPDATE_OFFENSE_CATEGORY': 'Offense Update'}
df.rename(columns=new_name, inplace = True)
df.head()
df.columns
df.shape
df2=df.copy()
df2.shape
df2.info()
df2.dropna(inplace=True)
df2.shape

df2['Offense'].value_counts()
df2 = df[(df['Offense'] == 'Burglary') | (df['Offense'] == 'Retail Theft') | (df['Offense'] == 'Narcotics') | (df['Offense'] == 'Homicide')].copy()
df2['Offense'].value_counts()
df2['Race'].value_counts()
df2 = df[(df['Race'] == 'Black') | (df['Race'] == 'White') | (df['Race'] == 'Hispanic') | (df['Race'] == 'Asian') | (df['Race'] == 'American Indian')].copy()
df2['Race'].value_counts()
df2['Review Result'].value_counts()
df2 = df[(df['Review Result'] == 'Approved') | (df['Review Result'] == 'Rejected') | (df['Review Result'] == 'Continued Investigation')].copy()
df2['Review Result'].value_counts()
df2['Offense Update'].value_counts()
df2 = df[(df['Offense Update'] == 'Burglary') | (df['Offense Update'] == 'Retail Theft') | (df['Offense Update'] == 'Narcotics') | (df['Offense Update'] == 'Homicide')].copy()
df2['Offense Update'].value_counts()
df2 = df[(df['Offense'] == 'Burglary') | (df['Offense'] == 'Retail Theft') | (df['Offense'] == 'Narcotics') | (df['Offense'] == 'Homicide')].copy()
df2['Offense'].value_counts()
sns.countplot(df2['Offense'])

df2 = df[(df['Offense Update'] == 'Burglary') | (df['Offense Update'] == 'Retail Theft') | (df['Offense Update'] == 'Narcotics') | (df['Offense Update'] == 'Homicide')].copy()
df2['Offense Update'].value_counts()
categorical = ['Race']
df2 = df[(df['Race'] == 'Black') | (df['Race'] == 'White') | (df['Race'] == 'Hispanic') | (df['Race'] == 'Asian') | (df['Race'] == 'American Indian')].copy()
df2['Race'].value_counts()
sorted_ou = df2.groupby(['Race'])['Age'].median().sort_values()
sns.boxplot(x=df2['Race'],y=df2['Age'], order=list(sorted_ou.index))

plot_by_offense = df2.groupby('Gender').size()
print(plot_by_offense)
plot_by_offense = plot_by_offense.plot(title='Total Number of Offenses grouped by Gender')
plot_by_offense.set_xlabel('Offenses')
plot_by_offense.set_ylabel('Count')
plt.xticks(rotation='vertical')

df2 = df[(df['Offense'] == 'Burglary') | (df['Offense'] == 'Retail Theft') | (df['Offense'] == 'Narcotics') | (df['Offense'] == 'Homicide')].copy()
df2['Offense'].value_counts()
sorted_ou = df2.groupby(['Offense'])['Age'].median().sort_values()
sns.boxplot(x=df2['Offense'],y=df2['Age'], order=list(sorted_ou.index))

df4 = df[(df['Review Result'] == 'Approved') | (df['Review Result'] == 'Rejected') | (df['Review Result'] == 'Continued Investigation')].copy()
df2['Review Result'].value_counts()
sorted_ou = df4.groupby(['Review Result'])['Age'].median().sort_values()
sns.boxplot(x=df4['Review Result'],y=df4['Age'], order=list(sorted_ou.index))
df2 = df[(df['Offense'] == 'Burglary') | (df['Offense'] == 'Retail Theft') | (df['Offense'] == 'Narcotics') | (df['Offense'] == 'Homicide')].copy()
df2['Offense'].value_counts()
df3 = df[(df['Race'] == 'Black') | (df['Race'] == 'White') | (df['Race'] == 'Hispanic') | (df['Race'] == 'Asian') | (df['Race'] == 'American Indian')].copy()
df2['Race'].value_counts()

grouped = df2.groupby(['Race','Offense'])
grouped.size()
g_offense = pd.crosstab(index=df2["Offense"],
                          columns=df2["Gender"])
g_offense
g_offense.plot(title='Top Four Offenses Committed by Gender',
                  kind="bar",
                  xlabel="Offense",
                  ylabel="Count",
                       figsize=(8,8),
                        stacked=True)
plt.xticks(rotation='vertical')

race_offense = pd.crosstab(index=df2["Offense"],
                          columns=df3["Race"])
race_offense
race_offense.plot(title='Top Four Offenses Committed by Race',
                  kind="bar",
                  xlabel="Offense",
                  ylabel="Count",
                       figsize=(8,8),
                        stacked=True)

plot_by_offense = df3.groupby('Race').size()
print(plot_by_offense)
plot_by_offense = plot_by_offense.plot(title='Total number of Offenses grouped by Race')
plot_by_offense.set_xlabel('Offenses')
plot_by_offense.set_ylabel('Count')
plt.xticks(rotation='vertical')

plot_by_offense = df4.groupby('Review Result').size()
print(plot_by_offense)
plot_by_offense = plot_by_offense.plot(title='Results of Convicted Offenders')
plot_by_offense.set_xlabel('Result')
plot_by_offense.set_ylabel('Count')
plt.xticks(rotation='horizontal')

