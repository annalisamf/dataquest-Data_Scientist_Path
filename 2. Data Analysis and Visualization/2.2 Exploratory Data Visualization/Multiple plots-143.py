## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt
# Read the file and convert the DATE colimn into a Series of datetime values.
unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
# Generate a line chart that visualizes the unemployment rates from 1948.
plt.plot(unrate['DATE'].head(12), unrate['VALUE'].head(12))
plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()

## 3. Matplotlib Classes ##

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

## 5. Adding Data ##

# Create 2 line subplots in a 2 row by 1 column layout:
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
# In the top subplot, plot the data from 1948.
ax1.plot(unrate['DATE'].head(12),unrate['VALUE'].head(12))
# In the bottom subplot, plot the data from 1949.
ax2.plot(unrate[12:24]['DATE'].head(12),unrate[12:24]['VALUE'].head(12))
plt.show()

## 6. Formatting And Spacing ##

# For the plot we generated in the last screen, set the width of the plotting area to 12 inches and the height to 5 inches.
fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

## 7. Comparing Across More Years ##

# plot five years of data.
fig = plt.figure(figsize=(12,12))

for i in range(5):
    ax = fig.add_subplot(5,1,i+1)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    ax.plot(subset['DATE'], subset['VALUE'])

plt.show()

## 8. Overlaying Line Charts ##

unrate['MONTH'] = unrate['DATE'].dt.month
# Set the plotting area to a width of 6 inches and a height of 3 inches.
fig = plt.figure(figsize=(6,3))
# Generate 2 line charts in the base subplot, using the MONTH column for the x-axis instead of the DATE column:
# One line chart using data from 1948, with the line color set to "red".
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c = 'red')
# One line chart using data from 1949, with the line color set to "blue".
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c = 'blue')
# Use plt.show() to display the plots.
plt.show()

## 9. Adding More Lines ##

# Let's visualize 5 years worth of unemployment rates on the same subplot.
# Generate the following plots in the base subplot:
# 1948: set the line color to "red"
# 1949: set the line color to "blue"
# 1950: set the line color to "green"
# 1951: set the line color to "orange"
# 1952: set the line color to "black"
# Use plt.show() to display the plots.
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i])
    
plt.show()

## 10. Adding A Legend ##

# Modify the code from the last screen that overlaid 5 plots to include a legend.
# Use the year value for each line chart as the label.
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label = str(1948 + i))
plt.legend(loc='upper left')
    
plt.show()

## 11. Final Tweaks ##

# Set the title to "Monthly Unemployment Trends, 1948-1952".
# Set the x-axis label to "Month, Integer".
# Set the y-axis label to "Unemployment Rate, Percent".

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")

plt.show()