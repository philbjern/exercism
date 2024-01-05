def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if (number < 1 or int(number) != number):
        raise ValueError("Classification is only possible for positive integers.")

    factors = []

    for num in range(1, number):
        if number % num == 0:
            factors.append(num)

    factor_sum = sum(factors)

    if factor_sum == number:
        return 'perfect'
    if factor_sum > number:
        return 'abundant'
    if factor_sum < number:
        return 'deficient'
