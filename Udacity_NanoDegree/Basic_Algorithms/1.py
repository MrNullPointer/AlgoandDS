def generate_numbers(num = 10):
    array = [i for i in range(num)]
    return array

def binary_search(array,number):
    if len(array) < 1:
        return False
    elif len(array) == 1:
        if array[0] == number:
            return True
        else:
            return False

    mid_val = len(array)//2
    if array[mid_val] == number:
        return True
    elif array[mid_val] > number:
        return binary_search(array[0:mid_val],number)
    else:
        return binary_search(array[mid_val:-1],number)
    return False;

array = generate_numbers(200)
guess = int(input("Guess the number: "))

if(binary_search(array,guess)):
    print("You got it!!")
else:
    print("Number not found")
