# Minimum cost to make array size 1 by removing larger of pairs
# Last Updated : 07 Jul, 2025
# Given an array of n integers. We need to reduce size of array to one. We are allowed to select a pair of integers and remove the larger one of these two. This decreases the array size by 1. Cost of this operation is equal to value of smallest one. Find out minimum sum of costs of operations needed to convert the array into a single element.

# Examples: 

# Input: arr[]= [4 ,3 ,2 ]
# Output: 4
# Explanation: Choose (4, 2) so 4 is removed, new array = {2, 3}. Now choose (2, 3) so 3 is removed.  So total cost = 2 + 2 = 4.

# Input: arr[]=[ 3, 4 ]
# Output: 3
# Explanation: choose (3, 4) so cost is 3. 

# Greedy Approach - Time O(n) and Space O(1)


def cost(a,n):
    return ((n-1)*min(a))

a=[4,3,2]
n=len(a)
print(cost(a,n))

def minicost(arr):
    n=len(arr)
    min_val=min(arr)
    total_cost = (n-1)*min_val
    return total_cost

arr = [4, 3, 2]
print(minicost(arr))