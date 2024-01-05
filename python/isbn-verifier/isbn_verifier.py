def is_valid(isbn):
    if 'P' in isbn:
        return False

    digits = [10 if i == "X" else int(i) for i in isbn if i.isdigit() or i == 'X']

    if len(digits) != 10:
        return False

    if 10 in digits and digits[-1] != 10:
        return False

    ex1 = 0
    for idx in range(0, len(digits)):
        ex1 = ex1 + digits[idx] * (len(digits) - idx)

    return ex1 % 11 == 0
