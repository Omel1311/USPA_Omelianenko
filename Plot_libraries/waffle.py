import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import seaborn_plots as sns
import numpy as np
import wordcloud
from PIL import Image
from pywaffle import Waffle
#_______________________________________________________________
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
#_______________________________________________________________
mpl.style.use('ggplot') # optional: for ggplot-like style
#_______________________________________________________________

df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
# print(df_can.head())
#_______________________________________________________________

print(df_can.shape)
df_can.set_index('Country', inplace=True)
#_______________________________________________________________

# let's create a new dataframe for these three countries
df_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden'], :]

# let's take a look at our dataframe
# print(df_dsn.head())
#_______________________________________________________________
#
# # compute the proportion of each category with respect to the total
total_values = df_dsn['Total'].sum()
print(total_values)
category_proportions = df_dsn['Total'] / total_values
# print(category_proportions.head())

print(df_dsn.head())
#
#
# # print out proportions
# print(pd.DataFrame({"Category Proportion": category_proportions}))
# #_______________________________________________________________
#
# width = 40 # width of chart
# height = 10 # height of chart
#
# total_num_tiles = width * height # total number of tiles
#
# print(f'Total number of tiles is {total_num_tiles}.')
# #_______________________________________________________________
#
# # compute the number of tiles for each category
# tiles_per_category = (category_proportions * total_num_tiles).round().astype(int)
#
# # print out number of tiles per category
# print(pd.DataFrame({"Number of tiles": tiles_per_category}))
# #_______________________________________________________________
# # initialize the waffle chart as an empty matrix
# waffle_chart = np.zeros((height, width), dtype=np.uint)
#
# # define indices to loop through waffle chart
# category_index = 0
# tile_index = 0
#
# # populate the waffle chart
# for col in range(width):
#     for row in range(height):
#         tile_index += 1
#
#         # if the number of tiles populated for the current category is equal to its corresponding allocated tiles...
#         if tile_index > sum(tiles_per_category[0:category_index]):
#             # ...proceed to the next category
#             category_index += 1
#
#             # set the class value to an integer, which increases with class
#         waffle_chart[row, col] = category_index
#
# print('Waffle chart populated!')
# print(waffle_chart)

#_______________________________________________________________
# # instantiate a new figure object
# fig = plt.figure()
#
# # use matshow to display the waffle chart
# colormap = plt.cm.coolwarm
# plt.matshow(waffle_chart, cmap=colormap)
# plt.colorbar()
# plt.show()
# #_______________________________________________________________
# # instantiate a new figure object
# fig = plt.figure()
#
# # use matshow to display the waffle chart
# colormap = plt.cm.coolwarm
# plt.matshow(waffle_chart, cmap=colormap)
# plt.colorbar()
#
# # get the axis
# ax = plt.gca()
#
# # set minor ticks
# ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
# ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
#
# # add gridlines based on minor ticks
# ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
#
# plt.xticks([])
# plt.yticks([])
# plt.show()
#_______________________________________________________________
# instantiate a new figure object
# fig = plt.figure()
#
# # use matshow to display the waffle chart
# colormap = plt.cm.coolwarm
# plt.matshow(waffle_chart, cmap=colormap)
# plt.colorbar()
#
# # get the axis
# ax = plt.gca()
#
# # set minor ticks
# ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
# ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
#
# # add gridlines based on minor ticks
# ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
#
# plt.xticks([])
# plt.yticks([])
#
# # compute cumulative sum of individual categories to match color schemes between chart and legend
# values_cumsum = np.cumsum(df_dsn['Total'])
# total_values = values_cumsum[len(values_cumsum) - 1]
#
# # create legend
# legend_handles = []
# for i, category in enumerate(df_dsn.index.values):
#     label_str = category + ' (' + str(df_dsn['Total'][i]) + ')'
#     color_val = colormap(float(values_cumsum[i]) / total_values)
#     legend_handles.append(mpatches.Patch(color=color_val, label=label_str))
#
# # add legend to chart
# plt.legend(handles=legend_handles,
#            loc='lower center',
#            ncol=len(df_dsn.index.values),
#            bbox_to_anchor=(0., -0.2, 0.95, .1)
#            )
# plt.show()
#_______________________________________________________________

#Set up the Waffle chart figure

fig = plt.figure(FigureClass = Waffle,
                 rows = 20, columns = 30, #pass the number of rows and columns for the waffle
                 values = df_dsn['Total'], #pass the data to be used for display
                 cmap_name = 'tab20', #color scheme
                 legend = {'labels': [f"{k} ({v})" for k, v in zip(df_dsn.index.values,df_dsn.Total)],
                            'loc': 'lower left', 'bbox_to_anchor':(0,-0.1),'ncol': 3}
                 #notice the use of list comprehension for creating labels
                 #from index and total of the dataset
                )

#Display the waffle chart
plt.show()







