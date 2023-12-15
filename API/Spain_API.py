def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."

# Example usage:
num1 = 10
num2 = 7

result1 = check_even_odd(num1)
result2 = check_even_odd(num2)

print(result1)
print(result2)