def power_of_2(input):
    if input <= 0:
        return 1

    output = power_of_2(input - 1)
    return 2 * output


def sum_of_integers(input):
    if input <= 0:
        return 0
    return input + sum_of_integers(input - 1)

def sum_array(array):
    if len(array) <= 0:
        return 0
    first_elem = array[0]
    return first_elem + sum_array(array[1:])

def sum_array_1(array):
    return sum_array_idx(array,0)

def sum_array_idx(array,idx):
    if len(array) == idx:
        return 0
    return array[idx] + sum_array_idx(array,idx + 1)

print(sum_array_1([1, 2, 3, 4]))
# print(sum_of_integers(30))
# print(power_of_2(10))
