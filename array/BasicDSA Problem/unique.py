# Unique Number I
# Last Updated : 23 Jul, 2025
# Given an array of integers, every element in the array appears twice except for one element which appears only once. The task is to identify and return the element that occurs only once.

# Examples: 

# Input:  arr[] = [2, 3, 5, 4, 5, 3, 4]
# Output: 2 
# Explanation: Since 2 occurs once, while other numbers occur twice, 2 is the answer.

# Input: arr[] = [2, 2, 5, 5, 20, 30, 30]
# Output: 20
# Explanation: Since 20 occurs once, while other numbers occur twice, 20 is the answer.

def unique_no(arr):
    result =0
    for num in arr:
        result ^= num
    return result

arr = [10, 7, 7, 3, 3, 10, 8]
print(unique_no(arr))