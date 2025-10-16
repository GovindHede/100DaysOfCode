# Generating All Subarrays
# Last Updated : 07 Feb, 2025
# Given an array arr[], the task is to generate all the possible subarrays of the given array.

# Examples: 

# Input: arr[] = [1, 2, 3]
# Output: [ [1], [1, 2], [2], [1, 2, 3], [2, 3], [3] ]

# Input: arr[] = [1, 2]
# Output: [ [1], [1, 2], [2] ]

def sub_array(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            for k in range(i,j+1):
                print(arr[k], end=" ")
            print()
arr = [1, 2, 3, 4]
print("All Non-empty Subarrays:")
sub_array(arr)

def all_subarray(arr):
    result =[]
    n= len(arr)
    for i in range(n):
        for j in range(i,n):
            result.append(arr[i:j+1])
    return result
arr = [1, 2, 3, 4]
print("All Non-empty Subarrays:")
for sub in all_subarray(arr):
    print(sub)