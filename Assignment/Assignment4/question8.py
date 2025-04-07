import pandas as pd

# Create two Series
series1 = pd.Series([10, 20, 30, 40, 50])
series2 = pd.Series([1, 2, 3, 4, 5])

# Addition
addition = series1 + series2

# Subtraction
subtraction = series1 - series2

# Multiplication
multiplication = series1 * series2

# Division
division = series1 / series2

# Print results
print("Series1:")
print(series1)
print("\nSeries2:")
print(series2)

print("\nAddition:")
print(addition)

print("\nSubtraction:")
print(subtraction)

print("\nMultiplication:")
print(multiplication)

print("\nDivision:")
print(division)
