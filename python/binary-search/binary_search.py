def find(search_list, value):
    if len(search_list) == 1 and search_list[0] == value:
        return 0

    if len(search_list) < 2:
        raise ValueError('value not in array')

    sorted_list = sorted(search_list)
    mid_idx = len(sorted_list) // 2
    idx = mid_idx
    middle_val = sorted_list[mid_idx]
    new_sublist = sorted_list

    while True:
        if middle_val < value:
            new_sublist = new_sublist[mid_idx:]
            mid_idx = len(new_sublist) // 2
            idx += mid_idx
            middle_val = new_sublist[mid_idx]

        elif middle_val > value:
            new_sublist = new_sublist[0:mid_idx]
            mid_idx = len(new_sublist) // 2
            idx = mid_idx
            middle_val = new_sublist[mid_idx]

        if middle_val == value:
            print(f'Value was found at index {idx}')
            break

        if len(new_sublist) <= 1 and middle_val != value:
            raise ValueError('value not in array')

    return idx


if __name__ == '__main__':
    find([1, 3, 4, 6, 8, 9, 11], 1)
