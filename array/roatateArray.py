#Roatate Array
def rotate_array(arr, k):   
    n = len(arr)
    k = k % n  # Handle cases where k is greater than n
    arr[:] = arr[-k:] + arr[:-k]  # Rotate the array in place
    return arr      

# Example usage
if __name__ == "__main__":      
    sample_array = [1, 2, 3, 4, 5]
    k = 2
    rotated_array = rotate_array(sample_array, k)
    print("Rotated Array:", rotated_array)  # Output: [4, 5, 1, 2, 3]

#explanation:
# The function rotate_array takes an array and an integer k as input.
# It calculates the effective rotation by taking k modulo the length of the array.
# The array is then rotated in place by slicing it into two parts: the last k elements