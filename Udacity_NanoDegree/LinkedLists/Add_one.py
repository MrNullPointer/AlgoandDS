def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits representing int (x + 1)
    """
    index = len(arr) -1
    while index >= 0:
        if arr[index] < 9:
            arr[index] += 1
            return arr
        else:
            arr[index] = 0
            if index > 0:
                index -= 1
            else:
                return [1] + arr
    return arr

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 9, 3, 9]
solution = [9, 9, 4, 0]
test_case = [arr, solution]
test_function(test_case)