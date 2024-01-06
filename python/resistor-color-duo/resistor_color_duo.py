def value(colors):
    number_values = [str(get_color_value(val)) for (idx, val) in enumerate(colors) if idx < 2]
    return int(''.join(number_values))


def get_color_value(color):
    values = ['black', 'brown', 'red',
              'orange', 'yellow', 'green',
              'blue', 'violet', 'grey', 'white']

    if color is None:
        return values
    elif color.lower() in values:
        return values.index(color.lower())

    return None
