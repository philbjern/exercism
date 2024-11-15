SINGLE_DIG = { 0: 'zero', 1: 'one', 2: 'two', 3: 'three',
               4: 'four', 5: 'five', 6: 'six', 7: 'seven',
               8: 'eight', 9: 'nine' }
 
TEENS = { 0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen',
            4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen',
            8: 'eighteen', 9: 'nineteen' }

TENS = { 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
        7: 'seventy', 8: 'eighty', 9: 'ninety' }

def say(number):
    if int(number) < 0 or int(number) > 999999999999:
        raise ValueError('input out of range')

    # single digits
    if int(number) < 10 and int(number) >= 0:
        print(single_digit(number))
        return single_digit(number)

    # teens
    if int(number) < 20 and int(number) >= 10:
        print(teens(number))
        return teens(number)

    # tens
    if int(number) >= 20 and int(number) < 100:
        num = TENS[int(number) // 10] 
        if int(number) % 10 != 0:
            num +='-' + single_digit(int(number) % 10)
        print(num)
        return num

    # hundreds
    if int(number) >= 100 and int(number) < 1000:
        num = single_digit(int(number) // 100) + ' hundred'
        if int(number) % 100 != 0:
            num += ' ' + say(int(number) % 100)
        print(num)
        return num

    # thousands
    if int(number) >= 1000 and int(number) < 1000000:
        num = say(int(number) // 1000) + ' thousand'
        if int(number) % 1000 != 0:
            num += ' ' + say(int(number) % 1000)
        print(num)
        return num

    # millions
    if int(number) >= 1000000 and int(number) < 1000000000:
        num = say(int(number) // 1000000) +' million'
        if int(number) % 1000000 != 0:
            num += ' ' + say(int(number) % 1000000)
        print(num)
        return num

    # billions
    if int(number) >= 1000000000 and int(number) < 1000000000000:
        num = say(int(number) // 1000000000) + ' billion'
        if int(number) % 1000000000 != 0:
            num += ' ' + say(int(number) % 1000000000)
        print(num)
        return num

def single_digit(number):
    return SINGLE_DIG[int(number)]

def teens(number):
    num = ''
    teens_part = int(number) // 10
    if teens_part == 1:
        num += TEENS[int(number) % 10] 
        return num

if __name__ == '__main__':
    say(-1)
    #say(0)
    #say(4)
    #say(14)
    #say(22)
    #say(129)
    #say(11329)
    #say(12345)
    #say(1234567890)

