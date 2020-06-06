def add_one(arr):
    if len(arr) == 0:
        return arr
    index = len(arr) - 1
    while True:
        if arr[index] < 9:
            arr[index] = arr[index] + 1
            return arr
        else:
            if index == 0:
                arr[index] = 0
                return [1] + arr
            arr[index] = 0
            index -= 1


arr1 = add_one([1,2,2,2,2,2,2])
arr2 = add_one([1,9,9,9,9,9,9,9])

print(arr2) 