def remove_duplicate(arr):
    if not arr:
        return []
    
    result= [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])

    return result
arr =[1, 2, 3]
print(remove_duplicate(arr))   
# you tryed best ok , as beginner you neild it , good job time O(n) and same Space O(n)
 #  *********************************************************************

# when we give interview at FAANG company the they except the space O(1) ands time O(n) complexity
#
def remove_duplicates(arr):
    if not arr:
        return 0
    
    # slow pointer points to last unique element
    j = 0
    
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    
    return j + 1  # length of distinct elements

# Example
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
length = remove_duplicates(arr)
print("Length:", length)
print("Array with distinct elements:", arr[:length])
