def nth_row_pascal(n):
    # base case
    if n < 2:
        return [1 for _ in range(n+1)]

    curr_list = [1 for _ in range(n+1)]
    prev_list = nth_row_pascal(n-1)
    first = 0
    second = first + 1
    for value in range(1,n):
        curr_list[value] = prev_list[first] + prev_list[second]
        first = first+1
        second = second + 1
    return curr_list


pascal_triangle = nth_row_pascal(180)

print(pascal_triangle)

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