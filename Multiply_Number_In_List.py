def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

a = [1, 3, 8, 6, 2]
print(multiply_list(a))