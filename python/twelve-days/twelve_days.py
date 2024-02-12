def recite(start_verse, end_verse):
    print(end_verse)
    print(start_verse)

    gifts = ('twelve Drummers Drumming', 'eleven Pipers Piping', 'ten Lords-a-Leaping',
             'nine Ladies Dancing', 'eight Maids-a-Milking', 'seven Swans-a-Swimming',
             'six Geese-a-Laying', 'five Gold Rings', 'four Calling Birds',
             'three French Hens', 'two Turtle Doves', 'a Partridge in a Pear Tree')

    lines = []

    for num in range(1, 12):
        line = 'On the '
        line += get_day_number(num)
        line += ' day of Christmas my true love gave to me: '

        day_gifts = gifts[(len(gifts) - num):]

        for index, gft in enumerate(day_gifts):
            if index < len(day_gifts) - 1 and index > 0:
                line += ', '
            elif index == len(day_gifts) - 1:
                line += ', and '
            line += gft

        lines.append(line)
        line = ''

    res = []

    for num in range(int(start_verse) - 1, int(end_verse)):
        print(lines[num])
        res.append(lines[num])

    return res


def get_day_number(day_number):
    days_strings = ['first', 'second', 'third', 'fourth',
                    'fifth', 'sixth', 'seventh', 'eighth'
                    'ninth', 'tenth', 'eleventh', 'twelfth']

    if day_number < 13 and day_number > 0:
        return days_strings[int(day_number) - 1]
    else:
        return 'None'
