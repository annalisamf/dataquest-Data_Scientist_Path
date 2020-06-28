## 2. Introduction to the data ##

import pandas as pd
# Read fandango_scores.csv into a Dataframe named reviews.
reviews = pd.read_csv('fandango_scores.csv')
# Select the following columns and assign the resulting Dataframe to norm_reviews:FILM, RT_user_norm ,Metacritic_user_nom (note the misspelling of norm), IMDB_norm, Fandango_Ratingvalue, Fandango_Stars
norm_reviews = reviews[['FILM','RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']]
# Display the first row in norm_reviews
norm_reviews

## 4. Creating Bars ##

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
# Create a single subplot and assign the returned Figure object to fig and the returned Axes object to ax.
fig, ax = plt.subplots()
# Generate a bar plot with:
    # left set to bar_positions
    # height set to bar_heights
    # width set to 0.5
ax.bar(bar_positions, bar_heights, 0.5)
plt.show()

## 5. Aligning Axis Ticks And Labels ##

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.5)
# Set the x-axis tick positions to tick_positions.
ax.set_xticks(tick_positions)
# Set the x-axis tick labels to num_cols and rotate by 90 degrees.
ax.set_xticklabels(num_cols, rotation=90)
# Set the x-axis label to "Rating Source".
ax.set_xlabel('Rating Source')
# Set the y-axis label to "Average Rating".
ax.set_ylabel('Average Rating')
# Set the plot title to "Average User Rating For Avengers: Age of Ultron (2015)".
ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')

plt.show()

## 6. Horizontal Bar Plot ##

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_widths = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()
ax.barh(bar_positions, bar_heights, 0.5)
# Set the y-axis tick positions to tick_positions.
ax.set_yticks(tick_positions)
# Set the y-axis tick labels to num_cols.
ax.set_yticklabels(num_cols)
# Set the y-axis label to "Rating Source".
ax.set_ylabel('Rating Source')
# Set the x-axis label to "Average Rating".
ax.set_xlabel('Average Rating')
# Set the plot title to "Average User Rating For Avengers: Age of Ultron (2015)".
ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')

plt.show()

## 7. Scatter plot ##

# Create a single subplot and assign the returned Figure object to fig and the returned Axes object to ax.
fig, ax = plt.subplots()
# Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the RT_user_norm column on the y-axis.
ax.scatter(norm_reviews['Fandango_Ratingvalue'],norm_reviews['RT_user_norm'])
# Set the x-axis label to "Fandango" and the y-axis label to "Rotten Tomatoes".
ax.set_xlabel('Fandango')
ax.set_ylabel('Rotten Tomatoes')
# Use plt.show() to display the resulting plot.
plt.show()


## 8. Switching axes ##

# Let's see what happens when we flip the columns
fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[cols]
# For the subplot associated with ax1:
# Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the RT_user_norm column on the y-axis.
ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
# Set the x-axis label to "Fandango" and the y-axis label to "Rotten Tomatoes".
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')
# For the subplot associated with ax2:
# Generate a scatter plot with the RT_user_norm column on the x-axis and the Fandango_Ratingvalue column on the y-axis.
ax2.scatter(norm_reviews['RT_user_norm'], norm_reviews['Fandango_Ratingvalue'])
# Set the x-axis label to "Rotten Tomatoes" and the y-axis label to "Fandango".
ax2.set_xlabel('Rotten Tomatoes')
ax2.set_ylabel('Fandango')
plt.show()


## 9. Benchmarking correlation ##

import matplotlib.pyplot as plt
#  Let's now generate scatter plots to see how Fandango ratings correlate with all 3 of the other review sites. 
fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

# For the Subplot associated with ax1:
# Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the RT_user_norm column on the y-axis.
ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
# Set the x-axis label to "Fandango" and the y-axis label to "Rotten Tomatoes".
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')
# Set the x-axis and y-axis data limits to range from 0 and 5.
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 5)
# For the Subplot associated with ax2:
# Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the Metacritic_user_nom column on the y-axis.
ax2.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['Metacritic_user_nom'])
# Set the x-axis label to "Fandango" and the y-axis label to "Metacritic".
ax2.set_xlabel('Fandango')
ax2.set_ylabel('Metacritic')
# Set the x-axis and y-axis data limits to range from 0 and 5.
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 5)
# For the Subplot associated with ax3:
# Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the IMDB_norm column on the y-axis.
ax3.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['IMDB_norm'])
# Set the x-axis label to "Fandango" and the y-axis label to "IMDB".
ax3.set_xlabel('Fandango')
ax3.set_ylabel('IMDB')
# Set the x-axis and y-axis data limits to range from 0 and 5.
ax3.set_xlim(0, 5)
ax3.set_ylim(0, 5)
plt.show()
