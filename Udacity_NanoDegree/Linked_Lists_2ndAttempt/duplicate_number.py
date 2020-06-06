def duplicate_number(arr):
    if arr is None:
        return
    current_sum = 0
    actual_sum = 0
    for val in arr:
        current_sum = current_sum + val

    for num in range(0,len(arr)-1):
        actual_sum = num + actual_sum
    return current_sum - actual_sum

arr = duplicate_number([0,1,2,3,8,4,5,6,7,3,9])
print(arr)
