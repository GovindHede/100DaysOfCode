
# Sum of all Subarrays
# Last Updated : 22 Jul, 2025
# Given an integer array arr[], compute the sum of all possible sub-arrays of the array. A sub-array is a contiguous part of the array.

# Examples: 

# Input: arr[] = [1, 4, 5, 3, 2]
# Output: 116
# Explanation: Sum of all possible subarrays of the array [1, 4, 5, 3, 2] is 116.

# Input: arr[] = [1, 2, 3, 4]
# Output: 50
# Explanation: Sum of all possible subarrays of the array [1, 2, 3, 4] is 50.


def sumof_subarr(arr):
    n =len(arr)
    result =0

    for i in range(n):
        result += arr[i]*(i+1)*(n-i)

    return result 

arr = [1,4,5,3,2]
print(sumof_subarr(arr))


# generating the Sub array

def make_subarrays(arr):
    n = len(arr)
    subarrays = []
    
    for i in range(n):
        for j in range(i, n):
            subarray = arr[i:j+1]
            subarrays.append(subarray)
    
    return subarrays

arr = [1, 4, 5, 3, 2]
print(make_subarrays(arr))
