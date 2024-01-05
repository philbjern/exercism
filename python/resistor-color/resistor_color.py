def color_code(color):
    codes = ['black', 'brown', 'red', 'orange',
             'yellow', 'green', 'blue',
             'violet', 'grey', 'white']

    if color is None:
        return codes

    if color.lower() in codes:
        return codes.index(color.lower())


def colors():
    return color_code(None)
