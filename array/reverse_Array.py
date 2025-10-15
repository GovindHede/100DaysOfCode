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
