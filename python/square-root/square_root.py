def square_root(number):
    value = 0
    old_val = number
    for n in range(10):
        value = 0.5 * (old_val + number / old_val)
        old_val = value

    return round(value)
