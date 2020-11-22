## 3. Introduction To The Data ##

import pandas as pd
import matplotlib.pyplot as plt


# Generate a line chart that visualizes the historical percentage of Biology degrees awarded to women:
#     Set the x-axis to the Year column from women_degrees.
#     Set the y-axis to the Biology column from women_degrees.
# Display the plot.


women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

plt.plot(women_degrees['Year'], women_degrees['Biology'])

## 4. Visualizing The Gender Gap ##

# Generate 2 line charts on the same figure:
#     One that visualizes the percentages of Biology degrees awarded to women over time. Set the line color to "blue" and the label to "Women".
#     One that visualizes the percentages of Biology degrees awarded to men over time. Set the line color to "green" and the label to "Men".
# Set the title of the chart to "Percentage of Biology Degrees Awarded By Gender".
# Generate a legend and place it in the "upper right" location.
# Display the chart.

plt.plot(women_degrees['Year'], women_degrees['Biology'], c='blue', label='Women')
plt.plot(women_degrees['Year'], 100-women_degrees['Biology'], c='green', label='Men')
plt.legend(loc='upper right')
plt.title('Percentage of Biology Degrees Awarded By Gender')
plt.show()


## 6. Hiding Tick Marks ##

# Generate 2 line charts in the same plotting area:
#     One that visualizes the percentages of Biology degrees awarded to women over time. Set the line color to "blue" and the label to "Women".
#     One that visualizes the percentages of Biology degrees awarded to men over time. Set the line color to "green" and the label to "Men".
# Remove all of the tick marks.
# Set the title of the plot to "Percentage of Biology Degrees Awarded By Gender".
# Generate a legend and place it in the "upper right" location.
# Display the chart.

plt.plot(women_degrees['Year'], women_degrees['Biology'], c='blue', label='Women')
plt.plot(women_degrees['Year'], 100-women_degrees['Biology'], c='green', label='Men')
plt.tick_params(bottom="off", top="off", left="off", right="off")
plt.title('Percentage of Biology Degrees Awarded By Gender')
plt.legend(loc='upper right')
plt.show()


## 7. Hiding Spines ##

fig, ax = plt.subplots()
ax.plot(women_degrees['Year'], women_degrees['Biology'], label='Women')
ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], label='Men')
ax.tick_params(bottom="off", top="off", left="off", right="off")
# Hide all of the spines.
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.legend(loc='upper right')
ax.set_title('Percentage of Biology Degrees Awarded By Gender')
plt.show()

## 8. Comparing Gender Gap Across Degree Categories ##

major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    ax.set_xlim([1968,2011])
    ax.set_ylim([0,100])
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    ax.set_title(major_cats[sp])

# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()