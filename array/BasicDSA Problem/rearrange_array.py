# Rearrange array such that even positioned are greater than odd
# Last Updated : 26 Nov, 2024
# Given an array arr[], sort the array according to the following relations:  

# arr[i] >= arr[i - 1], if i is even, ∀ 1 <= i < n
# arr[i] <= arr[i - 1], if i is odd, ∀ 1 <= i < n
# Find the resultant array.[consider 1-based indexing]

# Examples:  

# Input: arr[] = [1, 2, 2, 1]
# Output: [1 2 1 2]
#  Explanation:
# For i = 2, arr[i] >= arr[i-1]. So, 2 >= 1.
# For i = 3, arr[i] <= arr[i-1]. So, 1 <= 2.
# For i = 4, arr[i] >= arr[i-1]. So, 2 >= 1.

# Input: arr[] = [1, 3, 2]
# Output: [1 3 2]


def rearrange_arr(arr):
    arr.sort()

    for i in range(1,len(arr)):
        if (i+1) %2 ==0:
            if arr[i] < arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
        else:
            if arr[i] > arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
    return  arr

inputarr = [1,2,2,1]
result =rearrange_arr(inputarr)
print(result)