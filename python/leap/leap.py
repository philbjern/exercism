def leap_year(year):
    """
    Determines if input 'year' is a leap year
    year - input year to determine a leap for
    returns: Boolean (True if is a leap year, False otherwise)
    """

    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0
    divisible_by_400 = year % 400 == 0

    return divisible_by_4 and (not divisible_by_100 or divisible_by_400)
