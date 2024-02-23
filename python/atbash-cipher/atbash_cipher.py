def encode(plain_text):
    encoded = ''
    valid_char_count = 0
    for index, char in enumerate(plain_text):
        if char.isspace() or char == '.' or char == ',':
            continue
        if char.isupper():
            char = char.lower()

        if char.isnumeric():
            encoded += char

        if char.isalpha():
            code = ord(char) - ord('a')
            new_char = chr(ord('z') - code)
            encoded += new_char
        valid_char_count += 1

        if valid_char_count != 0 and valid_char_count % 5 == 0:
            encoded += ' '

    if encoded[-1] == ' ':
        encoded = encoded[:-1]

    return encoded


def decode(ciphered_text):
    decoded = ''
    for char in ciphered_text:
        if char.isupper():
            char = char.lower()

        if char.isspace():
            continue

        if char.isnumeric():
            decoded += char

        if char.isalpha():
            code = ord('z') - ord(char)
            new_char = chr(ord('a') + code)
            decoded += new_char

    return decoded
