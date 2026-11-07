def calculate_sum(n):

    if n <= 1:
        return n
    return calculate_sum(n-1)+n

number = 5

result = calculate_sum(number)

print("Sum:", result)