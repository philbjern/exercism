def is_isogram(string):
    letter_count = {}
    for l in string:
        if l.isalpha():
            letter_count[l.lower()] = letter_count.get(l.lower(), 0) + 1

    for count in letter_count:
        if letter_count[count] > 1:
            return False
    return True
