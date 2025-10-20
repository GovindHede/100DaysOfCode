# Minimum increment by k operations to make all equal
# Last Updated : 11 Oct, 2024
# You are given an array of n-elements, you have to find the number of operations needed to make all elements of array equal. Where a single operation can increment an element by k. If it is not possible to make all elements equal print -1.

# Example : 

# Input : arr[] = {4, 7, 19, 16},  k = 3
# Output : 10

# Input : arr[] = {4, 4, 4, 4}, k = 3
# Output : 0

# Input : arr[] = {4, 2, 6, 8}, k = 3
# Output : -1

# To solve this question we require to check whether all elements can became equal or not and that too only by incrementing k from elements value. For this we have to check that the difference of any two elements should always be divisible by k. If it is so, then all elements can become equal otherwise they can not became equal in any case by incrementing k from them. Also, the number of operations required can be calculated by finding value of (max - Ai)/k for all elements. where max is maximum element of array.

def miniOps(arr,n,k):
    max1 = max(arr)
    res =0

    for i in range(0,n):
        if ((max1-arr[i])%k!=0):
            return -1
        
        else:
            res +=(max1 - arr[i])/k
    return int(res)

arr=[21,33,9,45,63]
n=len(arr)
k=6
print(miniOps(arr,n,k))



def miniOps(arr,n,k):
    max1= max(arr)
    res =0
    for i in range(0,n):
        if (max1-arr[i])%k==0:
            return -1
        else:
            res += (max1-arr[i])/k
    return int(res)
