def answer(question):
    parsed = []

    if question.startswith('What is') and question.endswith('?'):
        question = question[len('What is'):-1]

    if len(question) == 0:
        raise ValueError('syntax error')

    question = question.replace('multiplied by', 'multiplied_by')
    question = question.replace('divided by', 'divided_by')

    words = question.strip().split()
    last = None

    for expr in words:
        if len(parsed) > 0:
            last = parsed[-1]

        if expr.isnumeric():
            if len(parsed) > 0 and is_number(last):
                raise ValueError('syntax error')
            else:
                parsed.append(expr)
        elif is_operation(expr):
            op = getoperator(expr)
            if op is None:
                raise ValueError('unknown operation')

            if is_parsed_operation(last):
                raise ValueError('syntax error')

            parsed.append(op)

    if is_parsed_operation(parsed[-1]):
        raise ValueError('syntax error')

    res = eval(''.join(parsed))
    print(''.join(parsed))
    print(res)

    return res


def is_number(expr):
    return expr.isnumeric()


def is_operation(expr):
    operations = ['plus', 'minus', 'multiplied_by', 'divided_by']
    return expr in operations


def is_parsed_operation(expr):
    parsed_op = ['+', '-', '*', '/']
    return expr in parsed_op


def getoperator(expr):
    if expr == 'plus':
        return '+'
    elif expr == 'minus':
        return '-'
    elif expr == 'multiplied_by':
        return '*'
    elif expr == 'divided_by':
        return '/'
    else:
        return None
