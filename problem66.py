import math

def is_perfect_square(n):
    """Check if a number is a perfect square."""
    return math.isqrt(n) ** 2 == n

def continued_fraction_sqrt(D):
    """Returns the continued fraction representation of sqrt(D)."""
    m, d, a0 = 0, 1, int(math.sqrt(D))
    if a0 * a0 == D:
        return []  # D is a perfect square, no solution needed
    a = a0
    period = []
    while a != 2 * a0:  # Period ends when we reach 2*a0
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d
        period.append(a)
    return [a0] + period

def solve_pell(D):
    """Finds the minimal solution (x, y) to x^2 - D*y^2 = 1 using continued fractions."""
    cf = continued_fraction_sqrt(D)
    if not cf:
        return None  # D is a perfect square

    a0, period = cf[0], cf[1:]
    h1, k1 = a0, 1
    h2, k2 = 1, 0  # Base cases
    a_list = period * 2  # Repeat period indefinitely

    for a in a_list:
        h = a * h1 + h2
        k = a * k1 + k2
        if h * h - D * k * k == 1:
            return (h, k)  # Found fundamental solution
        h2, k2 = h1, k1
        h1, k1 = h, k

    return None  # Should never reach here

# Take user input for D
try:
    max_D = int(input("Enter the maximum value of D: "))
    if max_D < 2:
        print("Please enter a value greater than or equal to 2.")
    else:
        max_x, best_D = 0, 0
        for D in range(2, max_D + 1):
            if is_perfect_square(D):  # Skip perfect squares
                continue
            solution = solve_pell(D)
            if solution and solution[0] > max_x:
                max_x, best_D = solution[0], D

        print(f"The value of D <= {max_D} that gives the largest minimal x is: {best_D}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
