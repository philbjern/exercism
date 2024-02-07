def flatten(iterable):
    output = []
    for item in iterable:
        if item is None:
            # ignore null values
            continue

        if type(item) is list:
            output.extend(flatten(item))
        else:
            output.append(item)

    return output
