# Move all Zeros to End of Array
# Last Updated : 03 Oct, 2025
# Given an array of integers arr[], move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.

# Examples: 

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.

# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.

# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.


def move_zero_end(arr):
    result =[]
    count_zero = 0
    for num in arr:
        if num !=0:
            result.append(num)
        else:
            count_zero +=1
    result.extend([0]* count_zero)
    return result
arr=[1, 2, 0, 4, 3, 0, 5, 0]
print(move_zero_end(arr))


def zero_moved(arr):
    j=0
    for i in  range(len(arr)):
        if arr[i] !=0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
    return arr