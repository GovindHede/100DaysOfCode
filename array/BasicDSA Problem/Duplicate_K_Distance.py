# Duplicate within K Distance in an Array
# Last Updated : 23 Jul, 2025
# Given an integer array arr[] and an integer k, determine whether there exist two indices i and j such that arr[i] == arr[j] and |i - j| ≤ k. If such a pair exists, return 'Yes', otherwise return 'No'.

# Examples: 

# Input: k = 3, arr[] = [1, 2, 3, 4, 1, 2, 3, 4]
# Output: No
# Explanation: Each element in the given array arr[] appears twice and the distance between every element and its duplicate is 4.

# Input: k = 3, arr[] = [1, 2, 3, 1, 4, 5]
# Output: Yes
# Explanation: 1 is present at index 0 and 3.

# Input: k = 3, arr[] = [1, 2, 3, 4, 5]
# Output: No
# Explanation: There is no duplicate element in arr[].

def Duplicate_k_Distance(arr,k):
    n=len(arr)

    for i in range(n):

        for c in range(1,k+1):
            j=i+c

            if j<n and arr[i] == arr[j]:
                return True
            
    return False

arr=[10, 5, 3, 4, 3, 5, 6]
k=3
print("yes" if Duplicate_k_Distance(arr,k) else "No")


def check_duplicate(arr,k):
    seen =set()
    for i in range(len(arr)):
        if arr[i] in seen:
            return True
        
        seen.add(arr[i])

        if i>=k:
            seen.remove(arr[i-k])
    return False