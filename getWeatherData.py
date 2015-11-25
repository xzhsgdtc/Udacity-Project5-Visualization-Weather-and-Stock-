# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:45:28 2015

@author: zihexu
"""

import csv
snow =[];
iceRain =[];
for i in range(-15,20):
    snow.append(0);
    iceRain.append(0);
#Open data for write 
with open('WeatherNY8.csv', 'wb') as outputcsv:
    a = csv.writer(outputcsv, delimiter=',');
#Add a title
    a.writerow(['lowTemp','snow','IceFog_Snow_Count','weather']);
#Open datafile as input
    with open('WeatherNY6.csv', 'rb') as csvfile:
         reader = csv.reader(csvfile, delimiter=',')
         reader.next();
         for row in reader:
#For each type add a row with correct typename
             if int(row[1])==1:
                 a.writerow([int(float(row[4])),int(row[1]),int(row[2]),'Snow_and_IceFog']);
             elif int(row[2])==1:
                 a.writerow([int(float(row[4])),int(row[1]),int(row[2]),'IceFog without Snow']);
             else:
                 a.writerow([int(float(row[4])),int(row[1]),int(row[2]),'Snow without IceFog']);

