def resistor_label(colors):

    resistor_colors = ['black', 'brown', 'red', 'orange',
                       'yellow', 'green', 'blue', 'violet',
                       'grey', 'white']

    tolerance_map = {'grey': '0.05%', 'violet': '0.1%', 'blue': '0.25%',
                     'green': '0.5%', 'brown': '1%', 'red': '2%',
                     'gold': '5%', 'silver': '10%'}

    PLUS_MINUS_SYMBOL = '±'

    print(colors)

    resistance_string = ''
    unit = 'ohms'
    tolerance = ''

    if len(colors) < 4:
        return '0 ohms'

    if len(colors) == 4:
        for index, band in enumerate(colors):
            if index <= 1:
                resistance_string = resistance_string + str(resistor_colors.index(band))

            if index == 2:
                resistance_string = resistance_string + "0" * resistor_colors.index(band)

            if index == 3:
                if band in tolerance_map:
                    tolerance = ' ' + PLUS_MINUS_SYMBOL + tolerance_map[band]
                else:
                    tolerance = ''

    elif len(colors) == 5:
        for index, band in enumerate(colors):
            if index <= 2:
                resistance_string = resistance_string + str(resistor_colors.index(band))

            if index == 3:
                resistance_string = resistance_string + '0' * resistor_colors.index(band)

            if index == 4:
                if band in tolerance_map:
                    tolerance = ' ' + PLUS_MINUS_SYMBOL + tolerance_map[band]
                else:
                    tolerance = ''

    resistance = int(resistance_string)

    if resistance >= 1_000_000_000:
        resistance = resistance / 1_000_000_000
        unit = 'giga' + unit
    elif resistance >= 1_000_000:
        resistance = resistance / 1_000_000
        unit = 'mega' + unit
    elif resistance >= 1000:
        resistance = resistance / 1000
        unit = 'kilo' + unit

    # resistance = round(100 * resistance) / 100
    if resistance == 2:
        resistance = '2'
    if resistance == 51:
        resistance = '51'

    res = f'{resistance} {unit}{tolerance}'

    return res
