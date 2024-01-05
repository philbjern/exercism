def is_armstrong_number(number):
    """
    Armstrong number is a number that is the sum of its own
    digits each raised to the power of the number of digits
    """
    digits = [int(i) for i in str(number)]
    sum_dig = sum(pow(i, len(digits)) for i in digits)

    return number == sum_dig
