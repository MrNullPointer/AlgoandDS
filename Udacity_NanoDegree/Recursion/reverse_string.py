# Code

def reverse_string(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """
    if len(input) <= 1:
        return input
    temp = len(input) - 1
    return input[temp] + reverse_string(input[:temp])

print(reverse_string("abc"))
print(reverse_string("hbdsgksfg sdgfnsg ghsbgs ghbgsdb g"))