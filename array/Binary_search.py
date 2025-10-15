#Iterative Binary Search Example:
def binary_search(arr,target):
    low,high = 0,len(arr) -1
    while low <= high:
        mid= (low +high)//2 #find the middle index
        if arr[mid] == target:
            return mid
        elif arr[mid]< target:
            low = mid+1
        else:
            high = mid -1
    return -1  # Target not found

#example usage
arr=[10,20,30,40,50,60]
target = 30
print(binary_search(arr,target))
# Output: 2
# Algorithm of Binary Search    
# 1. Start with two pointers: low at the beginning and high at the end of the array.
# 2. Calculate the middle index.    
# 3. If the middle element is equal to the target, return the index.
# 4. If the middle element is less than the target, move the low pointer to mid + 1.
# 5. If the middle element is greater than the target, move the high pointer to
# mid - 1.




#Recursive Binary Search Example:


def recursive_binary_search(arr, target,low, high):
    if low > high:
        return -1 # Base case : target not found
    
    mid = (low + high) //2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target,mid+1, high) # search right half
    else:
        return recursive_binary_search(arr,target,low,mid-1) #search left half

# Example usage
arr = [10, 20, 30, 40, 50, 60]
target = 40   
print(recursive_binary_search(arr, target, 0, len(arr) - 1))
  # Output: 2

# Algorithm of Recursive Binary Search
# 1. Check if the low pointer is greater than the high pointer. If so,  
# return -1 (base case).
# 2. Calculate the middle index.
# 3. If the middle element is equal to the target, return the index.
# 4. If the middle element is less than the target, recursively search the right half
# by adjusting the low pointer.
# 5. If the middle element is greater than the target, recursively search the left half
# by adjusting the high pointer.
