'''
The below approach uses the list permutation approach only with some minor modifications
'''

# def permutations(string):
#     """
#     :param: input string
#     Return - list of all permutations of the input string
#     TODO: complete this function to return a list of all permutations of the string
#     """
#     permute = list()    # create an empty list
#     if not string:      # if string is empty return
#         return
#     first_char = string[0]      # store the first character
#     sliced = slice(1,None)      # slice from the first to end
#     returned_string = permutations(string[sliced])  # recursively call
#     if not returned_string:         # condition when returned string is None
#         permute.append(first_char)
#         return permute
#     for elem in returned_string:        # iterate over the elements of returned list
#         for val in range(0,len(elem)+1):    # iterate over the length of individual elements
#             if val == 0:
#                 permute.append(first_char + elem)
#             else:
#                 head = slice(0,val)
#                 tail = slice(val,None)
#                 permute.append(elem[head] + str(first_char) + elem[tail])
#     return permute


'''
The approach below is provided in the solution of this problem
'''

def permutations(string):
    return short_permutes(string,0)

def short_permutes(string,index):
    if index >= len(string):
        return [""]
    returned_string = short_permutes(string,index + 1)
    permuted_list = list()
    indexed_char = string[index]
    for elem in returned_string:
        for val in range(0,len(elem)+1):
            temp = elem[0:val] + indexed_char + elem[val:]
            permuted_list.append(temp)
    return permuted_list

def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)