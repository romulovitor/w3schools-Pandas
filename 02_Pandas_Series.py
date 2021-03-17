import pandas as pd

# What is a Series?
a = [1, 7, 2]

var = pd.Series(a)

print(var, '\n')

# Labels
print([var[0]])
print([var[1]])
print([var[2]])

# Create Labels
var = pd.Series(a, index=['x', 'y', 'z'])
print(var, '\n')

print(var['y'], '\n')

# Key/Value Objects as Series
calories = {"day1": 420, "day2": 380, "day3": 390}

vay = pd.Series(calories)
print(vay, '\n')

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index=["day1", "day2"])

print(myvar)
