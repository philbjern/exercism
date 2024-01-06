def rows(letter):
    alphabet = ['A', 'B', 'C', 'D',
                'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X',
                'Y', 'Z']

    letter_idx = alphabet.index(letter)
    lines = []

    for i in range(letter_idx + 1):
        line = ''
        for j in range(letter_idx * 2 + 1):
            if j == (letter_idx - i) or j == (letter_idx + i):
                line = line + alphabet[i]
            else:
                line = line + ' '
        print(line)
        lines.append(line)

    for i in range(letter_idx + 1):
        if i == 0:
            continue
        line = ''
        width = letter_idx - i
        for j in range(letter_idx * 2 + 1):
            if j == letter_idx - width or j == letter_idx + width:
                line = line + alphabet[width]
            else:
                line = line + ' '
        print(line)
        lines.append(line)

    return lines
