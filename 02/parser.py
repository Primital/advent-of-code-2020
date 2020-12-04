def parse(row):
    parts = row.split(':')
    rules = parts[0].split('-')
    lb = int(rules[0])
    ub = int(rules[1].split(' ')[0])
    c = rules[1].split(' ')[1]
    pw = parts[1].lstrip(' ')
    return (lb, ub, c, pw)


def runner(content):
    valid_1 = 0
    valid_2 = 0
    for row in content:
        lb, ub, c, pw = parse(row)
        valid_1 += int(lb <= pw.count(c) <= ub)
        valid_2 += int((pw[lb - 1] == c) != (pw[ub - 1] == c))

    print(f"Valid password using first method: {valid_1}")
    print(f"                    second method: {valid_2}")


with open('data', 'r') as f:
    contents = f.read().split('\n')
    # last elem empty string, cba to deal with it
    runner(contents[:-1])
