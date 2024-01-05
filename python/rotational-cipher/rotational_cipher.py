KEY_DOMAIN = 26

ASCII_LOWER_START = 96
ASCII_LOWER_END = 122

ASCII_UPPER_START = 64
ASCII_UPPER_END = 90


def rotate(text, key):
    result = []
    for letter in text:
        if letter.isalpha() and letter.isupper():
            shifted = ord(letter) + (key % KEY_DOMAIN)
            if shifted > ASCII_UPPER_END:
                shifted = shifted % ASCII_UPPER_END + ASCII_UPPER_START
            result.append(chr(shifted))

        elif letter.isalpha() and letter.islower():
            shifted = ord(letter) + (key % KEY_DOMAIN)
            if shifted > ASCII_LOWER_END:
                shifted = shifted % ASCII_LOWER_END + ASCII_LOWER_START
            result.append(chr(shifted))

        else:
            result.append(letter)

    return ''.join(result)
