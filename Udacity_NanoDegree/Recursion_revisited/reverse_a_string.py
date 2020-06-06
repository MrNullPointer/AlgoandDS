def reverse_string(input):
    if len(input) == 0:
        return ''
    return reverse_string(input[1:]) + input[0]


print(reverse_string("abcdefghijklmnopqrstuvwxyz"))