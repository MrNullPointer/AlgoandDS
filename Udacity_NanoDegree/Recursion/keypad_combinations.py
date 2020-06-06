'''
Keypad Combinations
A keypad on a cellphone has alphabets for all numbers between 2 and 9.
You can make different combinations of alphabets by pressing the numbers.
For example, if you press 23, the following combinations are possible:
ad, ae, af, bd, be, bf, cd, ce, cf
Note that because 2 is pressed before 3, the first letter is always an alphabet on the number 2.
    Likewise, if the user types 32, the order would be
da, db, dc, ea, eb, ec, fa, fb, fc
Given an integer num, find out all the possible strings that can be made using digits of input num. Return these strings in a list.
        The order of strings in the list does not matter. However, as stated earlier, the order of letters in a particular string matters.
'''

def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


'''
My solution: Incorrect
'''

# def keypad(num):
#     # TODO: Write your keypad solution here!
#     if num <= 1:
#         return [""]
#     char_list = list()
#     while(num > 1):
#         rem = num % 10
#         char_list.append(get_characters(rem))
#         num = num // 10
#     returned = permutations(char_list[0],0)     # permuted list of the last digit
#     char_list.pop(0)
#     final_list = list()
#     for elem in range(0,len(char_list)):
#         for val in range(0,len(returned)):
#             temp = char_list[elem][val] + returned[val]
#             if temp not in final_list:
#                 final_list.append(temp)
#     return final_list
#
# def permutations(string,index):
#     if index >= len(string):
#         return [""]
#
#     return_permutation = permutations(string,index + 1)
#     permuted_list = list()
#     indexed_char = string[index]
#     for elem in return_permutation:
#         for val in range(0,len(elem)+1):
#             foo = elem[0:val] + indexed_char + elem[val:]
#             permuted_list.append(foo)
#     return permuted_list


'''
Udacity solution
'''

def keypad(num):
    if num <= 1:
        return [""]
    elif 1 < num <= 9:
        return list(get_characters(num))

    last_digit = num % 10
    small_output = keypad(num//10)
    keypad_string = get_characters(last_digit)
    output = list()
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            output.append(new_item)
    return output

def test_keypad(input, expected_output):
    if sorted(keypad(input)) == expected_output:
        print("Yay. We got it right.")
    else:
        print("Oops! That was incorrect.")


# Base case: list with empty string
input = 0
expected_output = [""]
test_keypad(input, expected_output)

# Example case
input = 23
expected_output = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
test_keypad(input, expected_output)

# Example case
input = 32
expected_output = sorted(["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"])
test_keypad(input, expected_output)

# Example case
input = 8
expected_output = sorted(["t", "u", "v"])
test_keypad(input, expected_output)

input = 354
expected_output = sorted(["djg", "ejg", "fjg", "dkg", "ekg", "fkg", "dlg", "elg", "flg", "djh", "ejh", "fjh", "dkh", "ekh", "fkh", "dlh", "elh", "flh", "dji", "eji", "fji", "dki", "eki", "fki", "dli", "eli", "fli"])
test_keypad(input, expected_output)
