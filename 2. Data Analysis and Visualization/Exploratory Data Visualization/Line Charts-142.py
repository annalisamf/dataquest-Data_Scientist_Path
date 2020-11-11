## 2. Introduction To The Data ##

# We've downloaded the monthly unemployment rate as a CSV from January 1948 to August 2016, saved it as unrate.csv, and made it available in this mission. 
import pandas as pd
unrate = pd.read_csv('unrate.csv')
# convert the DATE column into a series of datetime values
unrate['DATE']=pd.to_datetime(unrate['DATE'])
print(unrate.head(12))

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt
plt.plot()
plt.show()

## 7. Adding Data ##

# Generate a line chart that visualizes the unemployment rates from 1948. Display the plot.
x_values = unrate['DATE'].head(12)
y_values = unrate['VALUE'].head(12)
plt.plot(x_values, y_values)
plt.show()

## 8. Fixing Axis Ticks ##

# Generate the same line chart from the last screen that visualizes the unemployment rates from 1948.
x_values = unrate['DATE'].head(12)
y_values = unrate['VALUE'].head(12)
plt.plot(x_values, y_values)

# Use pyplot.xticks() to rotate the x-axis tick labels by 90 degrees. Display the plot.
plt.xticks(rotation=90)
plt.show()


## 9. Adding Axis Labels And A Title ##

# Generate the same line chart from the last screen that visualizes the unemployment rates from 1948.
x_values = unrate['DATE'].head(12)
y_values = unrate['VALUE'].head(12)
plt.plot(x_values, y_values)
plt.xticks(rotation=90)
# Set the x-axis label to "Month".
plt.xlabel('Month')
# Set the y-axis label to "Unemployment Rate".
plt.ylabel('Unemployment Rate')
# # Set the plot title to "Monthly Unemployment Trends, 1948".
plt.title('Monthly Unemployment Trends, 1948')
# Display the plot.
plt.show()