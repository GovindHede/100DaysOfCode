def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        # swapinng first and last element
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -= 1
    return arr

# Example usage
if __name__ == "__main__":  
    sample_array = [1, 2, 3, 4, 5]
    reversed_array = reverse_array(sample_array)
    print("Reversed Array:", reversed_array)  # Output: [5, 4, 3, 2, 1]


# Alogorithm:
# Initialize two pointers: start at the beginning (0 index) and end at the last element (length-1 index).

# Swap the elements at start and end.

# Increment start and decrement end.

# Repeat until start is greater than or equal to end.


def reverse_array(arr):
    satrt =0
    end =len(arr)-1
    while satrt < end :
        arr[satrt], arr[end] = arr[end], arr[satrt]
        satrt +=1
        end -=1
    return arr

# Array Reverse
# Last Updated : 08 Aug, 2025
# Reverse an array arr[]. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.

# Examples:

# Input: arr[] = [1, 4, 3, 2, 6, 5]  
# Output:  [5, 6, 2, 3, 4, 1]
# Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.

# Input: arr[] = [4, 5, 1, 2]
# Output: [2, 1, 5, 4]
# Explanation: The first element 4 moves to last position, the second element 5 moves to second last and so on.

def reved_arr(arr):
    start=0
    end =len(arr)-1

    while start < end:
        arr[start],arr[end] = arr[end], arr[start]
        start +=1
        end-=1
    return arr

arr = [1, 4, 3, 2, 6, 5]
print(reved_arr(arr))
