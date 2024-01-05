QUESTION_RESPONSE = "Sure."
YELLING_RESPONSE = "Whoa, chill out!"
YELLING_QUESTION_RESPONSE = "Calm down, I know what I'm doing!"
SILENCE_RESPONSE = "Fine. Be that way!"
WHATEVER_RESPONSE = "Whatever."


def response(hey_bob):
    stripped = hey_bob.strip()

    if ends_with_question_mark(stripped):
        if is_yelling(stripped):
            return YELLING_QUESTION_RESPONSE
        else:
            return QUESTION_RESPONSE
    elif is_yelling(stripped):
        return YELLING_RESPONSE
    elif is_silence(stripped):
        return SILENCE_RESPONSE

    return WHATEVER_RESPONSE


def ends_with_question_mark(text):
    if len(text) < 1:
        return False

    return text[-1] == "?"


def is_yelling(text):
    alpha = ''.join(e for e in text if e.isalpha())
    all_caps = alpha.isupper()
    return all_caps


def is_silence(text):
    return text is None or text == "" or text.isspace()
