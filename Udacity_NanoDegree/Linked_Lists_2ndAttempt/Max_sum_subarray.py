def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    if arr is None or len(arr) == 1:
        return arr

    running_sum = 0
    max_sum = 0
    for val in arr:
        running_sum = max(running_sum + val,val)
        max_sum = max(running_sum,max_sum)
    return max_sum

arr = max_sum_subarray([1, 2, 3, -4, 6])
print(arr)