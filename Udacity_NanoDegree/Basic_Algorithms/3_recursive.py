

def binary_search_recursive_soln(array, target, start_index, end_index):   
    if start_index > end_index:
        return -1
    
    mid_idx = (start_index + end_index) // 2
    if target == array[mid_idx]:
        return target
    elif target < array[mid_idx]:
        end_index = mid_idx - 1
        return binary_search_recursive_soln(array, target, start_index, end_index)
    else:
        start_index = mid_idx + 1
        return binary_search_recursive_soln(array, target, start_index, end_index)
    
    return -1




array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 11
index = 4

print(binary_search_recursive_soln(array,target,0,len(array)-1))