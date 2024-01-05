def label(colors):
    col_values = ['black', 'brown', 'red', 'orange',
              'yellow', 'green', 'blue', 'violet',
              'grey', 'white']

    numeric_values = []

    for index, col in enumerate(colors):
        if (index < 2):
            numeric_values.append(str(col_values.index(col.lower())))
        elif index == 2:
            zeros = '0' * col_values.index(col.lower())
            numeric_values.append(zeros)

    ohm_val = int(''.join(numeric_values))
    result = ''

    if ohm_val >= 1_000_000_000:
        result = str(ohm_val / 1_000_000_000)[:-2] + ' gigaohms'
    elif ohm_val >= 1_000_000:
        result = str(ohm_val / 1_000_000)[:-2] + ' megaohms'
    elif ohm_val >= 1000:
        result = str(ohm_val / 1000)[:-2] + ' kiloohms'
    else:
        result = str(ohm_val) + ' ohms'

    return result
