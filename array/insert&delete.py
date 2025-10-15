def insert_delete(arr):
    arr.append(4)
    print(f"After append :{arr}")

    arr.insert(1,3)
    print(f"After insert at index 1 :{arr}")

    arr.pop(0)
    print(f"After deletion at index 0:{arr}")

# Example usage
arr= [10,20,30]
insert_delete(arr)