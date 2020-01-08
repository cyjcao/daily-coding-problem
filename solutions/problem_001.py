# Asked by Google
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 17 is 17.
# Bonus: Can you do this in one pass?

def contains_pair(arr, k):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                return True
            
    return False

def contains_pair_one_pass(arr, k):
    # dictionary with keys = elements of the array and the corresponding value = k - key
    d = {} 
    for i in range(0, len(arr)):
        if k - arr[i] in d:
            return True
        else:
            d[arr[i]] =  k - arr[i]
    
    return False

ex_arr = [10, 15, 3, 7]
k = 17

# Test cases, should both return True
assert contains_pair(ex_arr, k)
assert contains_pair_one_pass(ex_arr, k)