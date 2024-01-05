def reverse(text):
    reversed = ""

    for i in range(len(text)):
        reversed = reversed + text[-i - 1]

    return reversed
