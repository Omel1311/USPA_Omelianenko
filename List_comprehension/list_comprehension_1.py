numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [x * x for x in numbers]

print(squares)

evan_numbers = [x for x in numbers if x % 2 != 0]

def is_evan(x):
    return x % 2 != 0

evan_numbers = [x for x in numbers if is_evan(x)]


print(evan_numbers)