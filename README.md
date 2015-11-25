# P6 Make Effective Data Visualization 
## Zihe Xu
##### Summary: In this project, I visualized the Weather data for New York. It contains the Highs and Lows and 15 kinds of hazard type. Of all those I found snow and Ice Fog is very interesting. From the data I have, it seems whenever it snows we have a ice fog, but the opposite is not true. Although might not be a causation, a strong connection between those two is clear. Also, I found all snows days have a temperature below 2 celsius, and the ice fog has a higher threshold, all of them happened below 4 celsius. 

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
I also create 3-day-average and 7-day-average to get a smooth line. 

### Design
First for the temperature, I choose to use circles to represent temperature as the position is the most accurate visual encoding, I also use color and size to distinguish 4 types of weather: \
- 1. Snow and Ice Fog
- 2. Snow without Ice Fog
- 3. Ice Fog without Snow
- 4. No Snow and no ice fog
Moreover to show reader the uplimit for both weather type, I use animation and some transparent rectangle to highlight the area where snow happens and the area the ice fog happens. 
At beginning there is an overview of all data which leave the reader a first impression of what I am presenting which a labeled line chart. Then I iterate through each year, and highlight 4 types of weather indicated above. Then at last, I will highlight the area important to snow and Ice fog.

### Feedback
There are so many iterations going on, and my friends gave a lot of questions I never think of. I will only list 3 of the most important one.These three corresponding to 3 versions I have.
From Han Pin
1. What do you notice in the visualization?\
The visualization shows a big trend of the NY's temperature
2. What questions do you have about the data?\
Where is these data coming from?
3. What relationships do you notice?\
New York is colder than my home town, even in the summer the highest is about 30 C. 
4. Is there something you don’t understand in the graphic?\
Why there is small points between 2013 and 2015.

This let me investigate the data further more and found that the data from 2014 to 2015 is not reliable, because on the Snow record it shows that there is not a single day has snow in a year, which is not right. So in the later analyze, I only use the first 4 years of data. 
Also I add color,animation after the first iteration.

From Amy
1. What do you notice in the visualization?\
The animation goes too fast. 
2. What questions do you have about the data?\
What does every color means? How frequent does the data collected?
3. What relationships do you notice?\
The world seems not getting warmer, at least new york 
4. Is there something you don’t understand in the graphic?\
What does the size of the circle means?

After this iteration, I add more description on the legend and changed their color based on the color shows on the screen, increased the time interval and make the smaller change of the size.

From Ya Nan 
1. What do you notice in the visualization?\
Not quite sure what message I should looking for.
2. What questions do you have about the data?\
Why there is no blue color?
3. What relationships do you notice?\
It seems both Ice Fog and the Snow only happened below certain temperature.
4. Is there something you don’t understand in the graphic?\
No.

In the final iteration, I add two square to indicate the temperature area for ice fog and snow to show that Snow and Ice fog only happens below certain temperature, and ice fog has a higher threshold. Also I add total number of four different type, to remind reader that there is no point shows snow but no ice fog, it seems whenever there is a snow, there is a ice fog. 

Although the data might not be a causation, but at least we can tell there is a strong connection between snow and ice fog sensor. they both happen under certain temperature, and ice fog is more often than snow. 


### Resources
- [National Centers for Environmental Information](http://www.ncdc.noaa.gov/)
- [Yahoo Finance](http://finance.yahoo.com/)




