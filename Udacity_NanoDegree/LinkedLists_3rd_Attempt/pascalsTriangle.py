def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    if n < 2:
        return [1 for _ in range(n + 1)]
    curr = [1 for _ in range(n + 1)]
    other_val = nth_row_pascal(n - 1)
    for i in range(1, n):
        curr[i] = other_val[i] + other_val[i - 1]
    return curr

print(nth_row_pascal(10))

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")


n = 0
solution = [1]
test_case = [n, solution]
test_function(test_case)

n = 1
solution = [1, 1]
test_case = [n, solution]
test_function(test_case)

n = 2
solution = [1, 2, 1]
test_case = [n, solution]
test_function(test_case)

n = 3
solution = [1, 3, 3, 1]
test_case = [n, solution]
test_function(test_case)

n = 4
solution = [1, 4, 6, 4, 1]
test_case = [n, solution]
test_function(test_case)
