def is_palindrome(input):
    return input == palindrome(input)

def palindrome(input):
    if len(input) == 1:
        return input
    return palindrome(input[1:]) + input[0]

print(is_palindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
# print(is_palindrome("p"))
# print ("Pass" if  (is_palindrome("abba")) else "Fail")