def convert(input_grid):

    if len(input_grid) % 4 != 0:
        raise ValueError('Number of input lines is not a multiple of four')

    if len(input_grid[0]) % 3 != 0:
        raise ValueError('Number of input columns is not a multiple of three')

    ocr_map = {
            0: [ord(' '), ord('_'), ord(' '),
                ord('|'), ord(' '), ord('|'),
                ord('|'), ord('_'), ord('|'),
                ord(' '), ord(' '), ord(' ')],

            1: [ord(' '), ord(' '), ord(' '),
                ord(' '), ord('|'), ord(' '),
                ord(' '), ord('|'), ord(' '),
                ord(' '), ord(' '), ord(' ')],

            2: [ord(' '), ord('_'), ord(' '),
                ord(' '), ord('_'), ord('|'),
                ord('|'), ord('_'), ord(' '),
                ord(' '), ord(' '), ord(' ')],
    }

    print(input_grid)

    """ parse ocr numbers from input_grid """
    numbers = [[]]

    for i, row in enumerate(input_grid):
        num_idx = 0
        for j, char in enumerate(row):
            if j % 3 == 0 and j != 0:
                num_idx += 1

            if len(row) // 3 > len(numbers):
                numbers.append([])

            numbers[num_idx].append(ord(char))

    ans = ''
    for num in numbers:
        for key, value in ocr_map.items():
            if value == num:
                ans += str(key)
                break

            if value == ocr_map[1]:
                print('found number one')

    print(ans)
    return ans
