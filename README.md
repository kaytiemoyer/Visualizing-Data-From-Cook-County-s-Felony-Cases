# Visualizing-Data-From-Cook-County-s-Felony-Cases
# Data-Visualization MSDS 670
## Project Overview
The Cook County State's Attorney's Office records and tracks thousands of felony cases every year. Starting in 2010 with State Attorney Fox, the open database houses hundreds of thousands of records of felony arrests, incarcerations, and probations. The file available for download held four files, each focusing on a separate part of the felony arrest and incarceration process. I focused on the "Initiation" or intake part of the process, where each person arrested was reported with their gender, race, arresting offence, and the results of those arrests ending in criminal charges or release. I wanted to answer the question of which demographics in Cook County are at the highest risk of being arrested and which areas of crime are the highest risks for those arrested. This could help to illustrate where social programs could help the most. 

## Data
#### Source: 
The data was taken from https://www.cookcountystatesattorney.org/data and sourced from the Cook County State's Attorney's Office records. Only the initiation.csv data set was used for this project. 
#### Scope: 
 The records involved in the inititiation.csv held over 42,000 reports of individuals who had been involved in felony charges and arrests. Each of these reports was sourced from a police officer employed with the Cook County Police Department, Sheriff Department, or State Troopers. 
## Process
This process was completed on a Windows 10 system, with  Python 3.9.0, Jupyter Notebook and Spyder IDE. 
#### 1.	Retrieving, cleaning and organizing the data. 
This involved downloading the data from the link provided and importing it into Spyder IDE for cleaning and testing with matplotlib. Columns with irrelevant data were dropped, n/a values were removed, and column names were renamed to simpler forms for easier callback later. Once this was completed, some tests were run in Spyder with both the seaborn and matplotlib package to experiment with different methods of graphing. This was later entered into Jupyter Notebook for easier editing with the graphs. 

#### 2.	Completing basic analysis of the data with the package matplotlib.
Comparisons graphed involved considering the top offenses categorized by the gender of the offender, the top offenses categorized by the race of the offender, and graphs depicting the results of the arrests; whether charges were pressed, charges were re-considered and revisited, or the charges were dropped below a felony. This will be updated next week with the completion and polishing of the graphs seen in the attached file.

The intake file was pushed to Github remotely, and is approximately 60 mb in size. A file containing the code is available for  both Spyder IDE and Jupyter Notebook for users to pick the IDE they wish to use to replicate the process above. 

## Visualizations (these descriptions will be edited in next week when presentations are finalized)
- Figure 1; Top 4 Offenses committed by Gender
- Figure 2; Top 4 Offenses committed by Race
- Figure 3; Results of the Reviewal Cases
- Figure 4, 5, 6; Total counts of reported gender, race and review cases 





