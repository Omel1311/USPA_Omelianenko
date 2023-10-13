import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import matplotlib as mpl


pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)
mpl.style.use(['default']) # optional: for ggplot-like style


'''
'default': The default style.
'classic': The classic style, similar to the old Matplotlib versions.
'bmh': The Bayesian Methods for Hackers style.
'fivethirtyeight': The style of plots used by FiveThirtyEight.
'seaborn': The Seaborn style, which is clean and modern.
'grayscale': A grayscale style.
'seaborn-colorblind': A style suitable for colorblind individuals.
'tableau-colorblind10': Tableau's colorblind-friendly palette.
'ggplot': The style emulates the aesthetics of plots made by the popular R package, ggplot2.
'dark_background': A style with a dark background, suitable for presentations or visualization in a dark environment.
'seaborn-darkgrid': A style with a dark grid from the Seaborn library.
'seaborn-whitegrid': A style with a white grid from the Seaborn library.
'seaborn-ticks': A style with tick marks from the Seaborn library.
'seaborn-poster': A style suitable for creating posters.
'''

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv"
df = pd.read_csv(URL)
print(df.head())
print(df.columns)
print(df.dtypes)


df['Year'] = pd.to_datetime(df['Date']).dt.year
df['Month'] = pd.to_datetime(df['Date']).dt.month


# line plot
# plt.figure(figsize=(12, 6))
# df_new = df.groupby('Year')['Estimated_fire_area'].mean()
#
# df_new.plot(x=df_new.index, y=df_new.values)
# plt.xlabel('Year')
# plt.ylabel('Average Estimated Fire Area (km²)')
# plt.title('Estimated Fire Area over Time')


# df_new_m = df.groupby(['Year', 'Month'])['Estimated_fire_area'].mean()
# df_new_m.plot(x=df_new_m.index, y=df_new_m.values)
# plt.xlabel('Year, Month')
# plt.xticks(rotation=45)
# plt.ylabel('Average Estimated Fire Area (km²)')
# plt.title('Estimated Fire Area over Time')
# # plt.show()
#
#
# # seaborn barplot
# plt.figure(figsize=(10, 6))
# sns.barplot(data=df, x='Region', y='Mean_estimated_fire_brightness')
# plt.xlabel('Region')
# plt.ylabel('Mean Estimated Fire Brightness (Kelvin)')
# plt.title('Distribution of Mean Estimated Fire Brightness across Regions')
#
#
# # pie chart
# plt.figure(figsize=(10, 6))
# region_counts = df.groupby('Region')['Count'].sum()
# plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%') #  autopct='%1.1f%%' to delete
# plt.title('Percentage of Pixels for Presumed Vegetation Fires by Region')
# plt.legend([(i,round(k/region_counts.sum()*100,2)) for i,k in zip(region_counts.index, region_counts)])
# plt.axis('equal')
#
#
# # histogram
# plt.figure(figsize=(10, 6))
# plt.hist(x=df['Mean_estimated_fire_brightness'], bins=20)
# plt.xlabel('Mean Estimated Fire Brightness (Kelvin)')
# plt.ylabel('Count')
# plt.title('Histogram of Mean Estimated Fire Brightness')


# histogram_2
sns.histplot(data=df, x='Mean_estimated_fire_brightness', hue='Region')
# hue='Region' specifies that we want to color the histogram bars based on the 'Region' variable.


# # histogram_3
# sns.histplot(data=df, x='Mean_estimated_fire_brightness', hue='Region', multiple='stack')
# plt.show()
#
#
# #sns.scatterplot()
# plt.figure(figsize=(8, 6))
# sns.scatterplot(data=df, x='Mean_confidence', y='Mean_estimated_fire_radiative_power')
# plt.xlabel('Mean Estimated Fire Radiative Power (MW)')
# plt.ylabel('Mean Confidence')
# plt.title('Mean Estimated Fire Radiative Power vs. Mean Confidence')
# plt.show()


# folium map
region_data = {'region':['NSW','QL','SA','TA','VI','WA','NT'],
               'Lat':[-31.8759835,-22.1646782,-30.5343665,-42.035067,-36.5986096,-25.2303005,-19.491411],
               'Lon':[147.2869493,144.5844903,135.6301212,146.6366887,144.6780052,121.0187246,132.550964]}
reg=pd.DataFrame(region_data)

# instantiate a feature group
aus_reg = folium.map.FeatureGroup()

# Create a Folium map centered on Australia
Aus_map = folium.Map(location=[-25, 135], zoom_start=4)

# loop through the region and add to feature group
for lat, lng, lab in zip(reg.Lat, reg.Lon, reg.region):
    aus_reg.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            popup=lab,
            radius=5, # define how big you want the circle markers to be
            color='red',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add incidents to map
Aus_map.add_child(aus_reg)
Aus_map.save('Austrlalia_wildfire_map.html')