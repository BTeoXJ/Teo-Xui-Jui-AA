def calculate_factorial(number):
    """Calculates the factorial of a non-negative integer."""

    if not isinstance(number, int):
        raise TypeError("Factorial input must be an integer.")

    if number < 0:
        raise ValueError("Factorial cannot be calculated for a negative number.")

    result = 1

    for value in range(2, number + 1):
        result *= value

    return result



