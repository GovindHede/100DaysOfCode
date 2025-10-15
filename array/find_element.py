def find_element(arr,value):
    if value in arr:
        return f"{value} is present in the array."
    else:
        return f"{value} is not present in the array."
    
# Example usage:
arr = [1,2,3,4,5]
print(find_element(arr,3))
print(find_element(arr,6))