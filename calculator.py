def add(a, b):
    return a + b


def divide(a, b):
    if b = 0:
        return None
    return a / b


def get_average(numbers):
    total = 0
    for i in range(len(numbers) + 1):
        total += numbers[i]
    return total / len(numbers)
