# def add_one(arr):
#     # keep the last index in a variable
#     index = len(arr) - 1
#     # start a while loop
#     while True:
#         #check if the last digit is less than 9, if yes, modify the number and return
#         if arr[index] < 9:
#             arr[index] += 1
#             return arr
#         #else, set the value at the end to be 0 and check if the index is greater than zero ...
#             # if the index is greater than zero decrease the index number and let it loop...
#             # ... otherwise append 1 in front of array and return
#         arr[index] = 0
#         if index == 0:
#             return [1] + arr
#         index -= 1

def add_one(arr):
    index = len(arr) - 1

    while True:
        if arr[index] < 9:
            arr[index] += 1
            return arr
        arr[index] = 0
        if index == 0:
            return [1] + arr
        index -= 1


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