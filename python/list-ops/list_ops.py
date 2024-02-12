def append(list1, list2):
    for item in list2:
        list1.append(item)

    return list1


def concat(lists):
    res = []
    for lis in lists:
        res.extend(lis)

    return res


def filter(function, list):
    res = []
    for item in list:
        if function(item):
            res.append(item)

    return res


def length(list):
    count = 0
    for item in list:
        count += 1

    return count


def map(function, list):
    mapped = []
    for item in list:
        mapped.append(function(item))

    return mapped


def foldl(function, list, initial):
    acc = initial
    for item in list:
        print(f'acc = {acc}, item = {item}')
        acc = function(acc, item)

    return acc


def foldr(function, list, initial):
    acc = initial
    for item in reversed(list):
        acc = function(acc, item)

    return acc


def reverse(list):
    res = []
    for item in reversed(list):
        res.append(item)

    return res
