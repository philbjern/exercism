BIT_ON = '1'


def commands(binary_str):
    bits = [i for i in binary_str]
    actions = []

    if bits[-1] == BIT_ON:
        actions.append('wink')
    if bits[-2] == BIT_ON:
        actions.append('double blink')
    if bits[-3] == BIT_ON:
        actions.append('close your eyes')
    if bits[-4] == BIT_ON:
        actions.append('jump')
    if bits[-5] == BIT_ON:
        actions.reverse()

    return actions
