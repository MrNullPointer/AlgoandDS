def sum_integers(num):
    if num == 1:
        return num
    return num + sum_integers(num-1)

print(sum_integers(3))

