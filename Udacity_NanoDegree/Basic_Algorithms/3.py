def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
   
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    start_idx = 0
    last_idx = len(array) - 1

    while start_idx <= last_idx:
        mid_idx = (start_idx + last_idx) // 2
        if target == array[mid_idx]:
            return mid_idx
        elif target < array[mid_idx]:
            last_idx = mid_idx - 1
        elif target > array[mid_idx]:
            start_idx = mid_idx + 1
    
    return -1

    while True:
        if len(array) <= 0:
            return -1
        mid_index = len(array) // 2
        idx += target
        if target == array[mid_index]:
            return mid_index
        if target < array[mid_index]:
            array = array[0:mid_index]
        elif target > array[mid_index]:
            array = array[mid_index+1:len(array)]
        else:
            return -1
    
    return -1





def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)