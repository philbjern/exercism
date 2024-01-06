def answer(question):
    print(question)
    answer = 0
    if question.startswith('What is') and question.endswith('?'):
        question = question[len('What is'):-1]
        print(len(question))
        if len(question) == 0:
            raise ValueError('syntax error')

        question = question.replace('multiplied by', 'multiplied_by')
        question = question.replace('divided by', 'divided_by')

        words = question.strip().split()
        print(words)
        operation = None
        supported_operations = ['plus', 'minus', 'multiplied_by', 'divided_by']
        prev = ''

        for index, expr in enumerate(words):
            if index == 0:
                answer = int(expr)
                prev = 'NUM'
            if index % 2 == 1:
                # Operation
                if expr not in supported_operations:
                    raise ValueError('unknown operation')
                operation = expr

            elif index % 2 == 0:
                # Operand
                try:
                    is(expr)
                except err:
                    raise ValueError('syntax error')

                if operation == 'plus':
                    answer = answer + int(expr)
                elif operation == 'minus':
                    answer = answer - int(expr)
                elif operation == 'multiplied_by':
                    answer = answer * int(expr)
                elif operation == 'divided_by':
                    answer = answer / int(expr)

    return answer
