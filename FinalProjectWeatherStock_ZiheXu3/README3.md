# P6 Make Effective Data Visualization 
## Zihe Xu
##### Summary: In this project, I visualized the Weather data for New York. It contains the Highs and Lows and 15 kinds of hazard type. Of all those I found snow and Ice Fog is very interesting. From the data I have,I found all snows days have a temperature below 2 celsius, and the ice fog has a higher threshold, all of them happened below 4 celsius. 

### 1. Find and clean the data
#### 1.1 Find data and basic attributes of the data
The Weather data comes from one station: NEW YORK CENTRAL PARK OBS BELVEDERE TOWER NY US. \
The weather data contains:
- Date - six numerical numbers(20150101)
- WT01 - Fog, ice fog, or freezing fog (may include heavy fog)
- WT02 - Heavy fog or heaving freezing fog (not always distinguished from fog)
- WT04 - Ice pellets, sleet, snow pellets, or small hail" 
- WT05 - Hail (may include small hail)
- WT06 - Glaze or rime 
- WT07 - Dust, volcanic ash, blowing dust, blowing sand, or blowing obstruction
- WT08 - Smoke or haze 
- WT09 - Blowing or drifting snow
- WT11 - High or damaging winds
- WT13 - Mist
- WT14 - Drizzle
- WT16 - Rain (may include freezing rain, drizzle, and freezing drizzle)" 
- WT17 - Freezing rain - 
- WT18 - Snow, snow pellets, snow grains, or ice crystals
- WT19 - Unknown source of precipitation 
- WT22 - Ice fog or freezing fog
- TMIN - Minimum temperature (tenths of degrees C)
- TMAX - Maximum temperature (tenths of degrees C) 

I also download the London weather data, however I found about half of the data is -9,999 which means null indicated by the NOAA's documentation. So I didn't include that. 
#### 1.2 Clean the data 
- 1. There are a lot of -9,999 in all columns starts from WT*, it means null or not happened. So I simply use find and replace in excel to replace all of those with 0.\
- 2. I Changed the column name from WT* to words reflect the meaning of that column and delete those with small number of records (Some of those smaller than 1)\

#### 1.3 Data Processing 
First notice most of the WT* means some kind of a bad weather, and normally 90% of them is 0, so I decide to look into those data individually and see what pattern it has. After carefully analyze, I found snow and the ice fog has a clear relation with temperature, especially the daily low, so I decided to look into them.
I use python to add categorical data as lables for further plotting. 

### Design
First for the temperature, I choose to use bar chart to represent how many times it snows and have ice fog in New York. Because it can show the amout of counts clearly. I labled Three of four types where at least Snow or ice fog was recorded.\
- 1. Snow and Ice Fog
- 2. Snow without Ice Fog
- 3. Ice Fog without Snow
- 4. No Snow and no ice fog
I use dimmple to draw the graph so simple animation interaction like hovering on the bar you can get the detail of that data.

### Feedback
There are so many iterations going on, and I changed my overall goal and how to plot many times. In the begining I tried a very big task to see the relation between weather and stock market. I failed that and tried complex graph with many animation to illustrate a simple relation, not good and now finally a simple graph with minium animation. I hope this time at least my graph is straight forward. 
From First grader
"Not able to find the correlation between stock prices and weather"

I changed my project to only focus on the weather data afterwards.
From the Second grader
"The visualization does include an animation, but I don't really consider it enhancing understanding of the data. "
I delete all unnecessary animation, only use the basic build-in interaction from dimmple 

Also, For this visulization, 
Jim suggest me to switch from area plots to bar plots.
Amy suggest me to ad a pie chart to better convey the idea: Ice fog happends more than snow. 
Liu suggest me to add a title at the end to explain the graph further more. 


### Resources
- [National Centers for Environmental Information](http://www.ncdc.noaa.gov/)
- [Yahoo Finance](http://finance.yahoo.com/)




