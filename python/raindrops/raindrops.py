def convert(number):
    result = ""

    if has_factor(number, 3):
        result = result + "Pling"
    if has_factor(number, 5):
        result = result + "Plang"
    if has_factor(number, 7):
        result = result + "Plong"

    if not has_factor(number, 3) and not has_factor(number, 5) and not has_factor(number, 7):
        result = str(number)

    return result


def has_factor(number, factor):
    return number % factor == 0
