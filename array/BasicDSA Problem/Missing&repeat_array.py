# Missing and Repeating in an Array
# Last Updated : 23 Jul, 2025
# Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find both the duplicate number and the missing number.

# Examples: 

# Input: arr[] = [3, 1, 3]
# Output: [3, 2]
# Explanation: 3 is occurs twice and 2 is missing.

# Input: arr[] = [4, 3, 6, 2, 1, 1]
# Output: [1, 5] 
# Explanation: 1 is occurs twice and 5 is missing.

def findTwoElement(arr):
    n= len(arr)

    freq =[0] * (n+1)
    repeating = -1
    missing = -1

    for num in arr:
        freq[num] +=1

    for i in range(1,n+1):
        if freq[i] ==0:
            missing =i
        elif freq[i] ==2:
            repeating =i

    return [repeating, missing]

arr= [3, 1, 3]
ans = findTwoElement(arr)
print(ans[0],ans[1])

