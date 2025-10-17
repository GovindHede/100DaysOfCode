# Generating All Subarrays
# Last Updated : 07 Feb, 2025
# Given an array arr[], the task is to generate all the possible subarrays of the given array.

# Examples: 

# Input: arr[] = [1, 2, 3]
# Output: [ [1], [1, 2], [2], [1, 2, 3], [2, 3], [3] ]

# Input: arr[] = [1, 2]
# Output: [ [1], [1, 2], [2] ]

def sub_array(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            for k in range(i,j+1):
                print(arr[k], end=" ")
            print()
arr = [1, 2, 3, 4]
print("All Non-empty Subarrays:")
sub_array(arr)

def all_subarray(arr):
    result =[]
    n= len(arr)
    for i in range(n):
        for j in range(i,n):
            result.append(arr[i:j+1])
    return result
arr = [1, 2, 3, 4]
print("All Non-empty Subarrays:")
for sub in all_subarray(arr):
    print(sub)



a = 2
b=3
print("a=",a,"b=",b)

temp = a 
a=b
b = temp

print("a=",a,"b=",b)

#Find Closest to n and Divisible by m

def closed_ele(n,m):
    a = (n//m) *m
    b= a+m
    if abs(n-a) < abs(n-b):
        return a
    elif abs(n-a) > abs(n-b):
        return b
    else:
        return a if abs(a) >abs(b) else b
    
print(closed_ele(13,4))
print(closed_ele(-15,6))


def dice_num(n):
    if n ==1:
        return 6
    elif n==2:
        return 5
    elif n==3:
        return 4
    elif n==6:
        return 1
    elif n==4:
        return 3
    elif n==5:
        return 2

n=6
print(dice_num(n))    

def dice_oppo(n):
    ans =7-n
    return ans
n=6
print(dice_oppo(n))

def nthterm(a1,a2,n):
    nthTerm = a1
    d = a2-a1
    for i in range(1,n):
        nthTerm +=d
    return nthTerm

a1=2
a2 =3
n=4
print(nthterm(a1,a2,n))