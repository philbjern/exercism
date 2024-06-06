from math import sqrt

def cipher_text(plain_text):
    if plain_text == '':
        return ''

    normalized = ''
    for ch in plain_text:
        if ch in ('.', ',', '\'', '"', '?', '!', ' ', '@', '%', '-'):
            continue
        normalized += ch.lower()

    if len(normalized) == 0:
        return ''

    if len(normalized) == 1:
        return normalized

    # Calculate rectangle dimentions
    r, c = calculateRectangle(normalized)

    # Create square lines
    squared = ['']
    idx = 0
    for ch in normalized:
        if len(squared[idx]) < c:
            squared[idx] += ch
        else:
            squared.append(ch)
            idx += 1

    # Get encoded lines
    encoded_list = []
    idx = 0

    for i in range(0, c):
        encoded_list.append('')
        for st in squared:
            if len(st) >= idx + 1:
                encoded_list[idx] += st[idx]
            else:
                encoded_list[idx] += ' '
        idx += 1

    return ' '.join(encoded_list)


def calculateRectangle(str):
    length = len(str)
    r_candid = round(sqrt(length))
    c_candid = round(length / r_candid)

    valid = True
    if r_candid * c_candid < length:
        valid = False

    if c_candid < r_candid:
        valid = False

    if c_candid - r_candid > 1:
        valid = False

    if valid:
        return (r_candid, c_candid)
