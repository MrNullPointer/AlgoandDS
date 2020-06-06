def is_palindrome(input):
    if len(input) <= 1:
        return True
    if input[0] == input[len(input)-1]:
        return is_palindrome(input[1:(len(input)-1)])
    else:
        return False

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")
print ("Pass" if not (is_palindrome("UdacityadU")) else "Fail")