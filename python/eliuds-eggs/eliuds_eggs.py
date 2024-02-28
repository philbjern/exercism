def egg_count(display_value):
    binary_str = to_binary(display_value)

    bit_sum = 0
    for bit in binary_str:
        if bit == '1':
            bit_sum += 1

    return bit_sum


def to_binary(number):
    binary_str = ''
    ''' convert number to binary string '''
    while number > 0:
        binary_str = str(number % 2) + binary_str
        number = number // 2

    return binary_str
