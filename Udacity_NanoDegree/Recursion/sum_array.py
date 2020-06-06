def sum_array(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_array(arr[1:])



# def sum_array(arr,index):
#     if len(arr) - 1 == index:
#         return arr[index]
#     return arr[index] + sum_array(arr,index + 1)

arr = [1,2,3,4,5,6,2,3,4,5,545,6,6,76,66,454,5,4,43,3,4,5]
print(sum_array(arr))