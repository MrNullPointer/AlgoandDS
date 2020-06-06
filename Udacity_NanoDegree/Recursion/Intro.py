'''Just Practice'''

def recursion(input):
    if input <= 0:
        return input + 1
    else:
        output = 0
        output += recursion(input - 1)
        return output

foo = recursion(3)
print(foo)