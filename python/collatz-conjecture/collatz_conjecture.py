def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    steps_num = 0
    return collatzConjecture(number, steps_num)


def collatzConjecture(number, number_steps):
    """
    Recursive function to calculate number of steps
    needed for a number to reach Collatz Conjecture
    (reach 1)
    """
    if number == 1:
        return number_steps

    if number % 2 == 0:
        number = number / 2
    else:
        number = 3 * number + 1

    number_steps = number_steps + 1

    return collatzConjecture(number, number_steps)
