def get_alphabet(num):
    return chr(96 + num)

def all_codes(number):
    if number == 0:
        return [""]
    remainder = number % 100
    list_100 = list()

    if remainder > 9 and remainder < 27:
        remainder_alpha = get_alphabet(remainder)
        list_100 = all_codes(number//100)
        for idx,elem in enumerate(list_100):
            list_100[idx] = elem + remainder_alpha

    remainder = number % 10
    list_10 = all_codes(number//10)
    remainder_alpha = get_alphabet(remainder)
    for idx,elem in enumerate(list_10):
        list_10[idx] = elem + remainder_alpha

    output = list()
    output.extend(list_100)
    output.extend(list_10)
    return output

def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]

    output = all_codes(number)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


number = 123
solution = ['abc', 'aw', 'lc']
test_case = [number, solution]
test_function(test_case)

number = 145
solution =  ['ade', 'ne']
test_case = [number, solution]
test_function(test_case)

number = 1145
solution =  ['aade', 'ane', 'kde']
test_case = [number, solution]
test_function(test_case)

number = 4545
solution = ['dede']
test_case = [number, solution]
test_function(test_case)

