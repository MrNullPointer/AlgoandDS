def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    if n < 2:
        return [1 for _ in range(n+1)]
    output = [1 for _ in range(n+1)]
    previous = nth_row_pascal(n-1)
    first = 0
    second = 1
    for index in range(1, n):
        output[index] = previous[first] + previous[second]
        first = first + 1
        second += 1
    return output

x = nth_row_pascal(0)
print(x)