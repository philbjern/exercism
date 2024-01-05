def square(number):
    """
    Returns number of grains on a given square number of the
    chessboard. Each square has double the grains on the
    previous square.
    """

    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return pow(2, number - 1)


def total():
    """
    Total number of grains on all chessboard squares.
    """

    sum = 0
    for index in range(1, 65):
        sum = sum + square(index)

    return sum
