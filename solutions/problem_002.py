# This problem was asked by Uber
#
# Given an array of integers, return a new array such that each element at index i of the new array is 
# the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

def create_products_arr(arr):
    product = 1
    for i in range(0, len(arr)):
        product = product * arr[i]
    
    products_arr = []
    for j in range(0, len(arr)):
        products_arr.append(int(product / arr[j]))
    
    return products_arr


def create_products_arr_no_div(arr):
    products_arr = []
    for i in range(0, len(arr)):
        product = 1
        for j in range(0, len(arr)):
            if j != i:
                product = product * arr[j]
        
        products_arr.append(product)
    
    return products_arr


# Test case, function should return [120, 60, 40, 30, 24]
assert create_products_arr([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert create_products_arr_no_div([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]