## 1. Reading CSV files with NumPy ##

import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')
taxi_shape=taxi.shape

## 2. Reading CSV files with NumPy Continued ##

import numpy as np
taxi=np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=1)
taxi_shape=taxi.shape

## 3. Boolean Arrays ##

a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])
a_bool=a<3
b_bool=b=='blue'
c_bool=c>100

## 4. Boolean Indexing with 1D ndarrays ##

pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides =  january.shape[0]

february_bool=pickup_month==2
february=pickup_month[february_bool]
february_rides=pickup_month[pickup_month==2].shape[0]
print(february_rides)

## 5. Boolean Indexing with 2D ndarrays ##

# calculate the average speed
trip_mph = taxi[:,7] / (taxi[:,8] / 3600)

# create a boolean array for trips with average
# speeds greater than 20,000 mph
trip_mph_bool = trip_mph > 20000

# use the boolean array to select the rows for
# those trips, and the pickup_location_code,
# dropoff_location_code, trip_distance, and
# trip_length columns
trips_over_20000_mph = taxi[trip_mph_bool,5:9]


tip_bool= taxi[:,12]>50
top_tips=taxi[tip_bool,5:14]

## 6. Assigning Values in ndarrays ##

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()
# The value at column index 5 (pickup_location) of row index 28214 is incorrect. Use assignment to change this value to 1 in the taxi_modified ndarray.
taxi_modified[28214,5] = 1

# The first column (index 0) contains year values as four digit numbers in the format YYYY (2016, since all trips in our data set are from 2016). Use assignment to change these values to the YY format (16) in the taxi_modified ndarray.
taxi_modified[:,0]=16

# The values at column index 7 (trip_distance) of rows index 1800 and 1801 are incorrect. Use assignment to change these values in the taxi_modified ndarray to the mean value for that column.

taxi_modified[1800:1802,7]=taxi_modified[:,7].mean()


## 7. Assignment Using Boolean Arrays ##

# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()

# Select the fourteenth column (index 13) in taxi_copy. Assign it to a variable named total_amount.
total_amount=taxi_copy[:,13]
total_amount[total_amount<0]=0

## 8. Assignment Using Boolean Arrays Continued ##

# create a new column filled with `0`.
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)

taxi_modified[taxi_modified[:,5]==2,15]=1
taxi_modified[taxi_modified[:,5]==3,15]=1
taxi_modified[taxi_modified[:,5]==5,15]=1

## 9. Challenge: Which is the most popular airport? ##

# In this challenge, we want to figure out which airport is the most popular destination in our data set. To do that, we'll use boolean indexing to create three filtered arrays and then look at how many rows are in each array. 
jfk=taxi[taxi[:,6]==2]
jfk_count=jfk.shape[0]

laguardia=taxi[taxi[:,6]==3]
laguardia_count=laguardia.shape[0]

newark=taxi[taxi[:,6]==5]
newark_count=newark.shape[0]


## 10. Challenge: Calculating Statistics for Trips on Clean Data ##

trip_mph = taxi[:,7] / (taxi[:,8] / 3600)
cleaned_taxi=taxi[trip_mph<100]
mean_distance=cleaned_taxi[:,7].mean()
mean_length=cleaned_taxi[:,8].mean()
mean_total_amount=cleaned_taxi[:,13].mean()