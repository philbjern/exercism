def square_of_sum(number):
    sum = 0
    for num in range(1, number + 1):
        sum += num

    print(f'1) number = {number}, sum = {sum}')
    return pow(sum, 2)


def sum_of_squares(number):
    sum = 0
    for num in range(1, int(number) + 1):
        sum = sum + pow(num, 2)

    print(f'2) number = {number}, sum = {sum}')
    return sum


def difference_of_squares(number):
    diff = square_of_sum(number) - sum_of_squares(number)
    print(f'3) diff = {diff}')
    return diff
