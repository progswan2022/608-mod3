# Bonus script

# import random module
import random as rand

# import statistics module
import statistics as stat

# define a list from which random values can be gathered (1-999)
list1 = range(0, 1000)

# Use sample function to choose 100 values from list1
list2 = rand.sample(list1,100)

# Print list2
print(list2)

# calculate variance
print(f'Population Variance of random set of 100 integers between 0 and 999:', stat.pvariance(list2))

# calulate standard deviation
print(f'Population Standard Deviation of random set of 100 integers between 0 and 999:', stat.pstdev(list2))

print('Erin Swan-Siegel')