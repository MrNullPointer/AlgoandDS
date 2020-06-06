# Code

import copy


def permute(l):
    """
    Return a list of permutations

    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]

    Args:
      l(list): list of items to be permuted

    Returns:
      list of permutation with each permuted item being represented by a list
    """
    if len(l) <= 0:
        return [[]]

    returned_list = permute(l[1:])
    first_digit = l[0]
    perm = list()

    for elem in returned_list:
        for val in range(len(elem) + 1):
            temp = copy.deepcopy(elem)
            temp.insert(val,first_digit)
            perm.append(temp)
    return perm








# Test Cases

# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e


print("Pass" if (check_output(permute([]), [[]])) else "Fail")
print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print("Pass" if (
    check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")