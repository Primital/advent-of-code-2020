import functools


def combined_answers(groups):
    result = 0
    for group in groups:
        answers = group[1]
        combined = ''.join(answers)
        result += len(list(set(combined)))
    return result


def unique_answers(groups):
    result = 0
    for group in groups:
        answers = group[1]
        combined = [set(answer) for answer in answers]
        unique = functools.reduce(lambda a, b: a.intersection(b), combined)
        result += len(list(unique))
    return result


# RUNNER
def runner(path):
    n = 0
    forms = []
    groups = []
    with open(path, 'r') as f:
        for row in f.read().split('\n'):
            if row == '':
                groups.append((n, forms))
                forms = []
                n = 0
            else:
                n += 1
                forms.append(row)
    # Problem 1
    print(combined_answers(groups))
    # Problem 2
    print(unique_answers(groups))


runner('./data')
