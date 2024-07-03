#!/usr/bin/env python3

"""
This script imports the sum_mixed_list function from the module 6-sum_mixed_list
and tests it with a list of mixed numbers.
"""

# Import the sum_mixed_list function
sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

# Print the annotations of the sum_mixed_list function
print(sum_mixed_list.__annotations__)

# Define a list of mixed numbers
mixed = [5, 4, 3.14, 666, 0.99]

# Call the sum_mixed_list function with the mixed list
ans = sum_mixed_list(mixed)

# Check if the sum of the mixed list is equal to the result of the sum_mixed_list function
print(ans == sum(mixed))

# Print the result of the sum_mixed_list function along with its type
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
