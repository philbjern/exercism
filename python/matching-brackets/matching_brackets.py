def is_paired(input_string):
    opening_brackets = "([{"
    closing_brackets = ")]}" 
    brackets = dict(zip(opening_brackets, closing_brackets))
    stack = []

    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or brackets[stack.pop()] != char:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(is_paired("{}()({{}})"))
    print(is_paired("{}()({{}}"))
