# Check if an Array is Sorted
# Last Updated : 11 Oct, 2025
# Given an array arr[], check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.

# Examples: 

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: true
# Explanation: The given array is sorted.

# Input: arr[] = [90, 80, 100, 70, 40, 30]
# Output: false
# Explanation: The given array is not sorted.

def check_sorted_arr(arr):
    return arr == sorted(arr)
    

arr = [10,20,30,40,50]
if check_sorted_arr(arr):
    print("true")
else:
    print("flase")



def issorted(arr):
    n= len(arr)
    for i in range(1,n):
        if (arr[i-1]>arr[i]):
            return False
    return True

arr = [10,20,30,40,50]
if issorted(arr):
    print("true")
else:
    print("flase")