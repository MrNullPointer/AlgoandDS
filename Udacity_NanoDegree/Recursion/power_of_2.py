def pow(exponent):
    if exponent <= 1:
        return 2
    else:
        output = pow(exponent - 1)
        output *= 2
        return output

result = pow(5)
print(result)