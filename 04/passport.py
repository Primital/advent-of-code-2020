import functools

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] 

def extract_passports(data):
    passports = []
    tmp = []
    for row in data:
        if len(row) == 0:
            passports.append(' '.join(tmp))
            tmp = []
        else:
            tmp.append(row)
    else:
        if len(tmp):
            passports.append(tmp)
    return passports


def separate_fields(passport):
    if len(passport) == 0:
        return []
    fields = passport.split(' ')
    return fields


def validate_passports(data):
    extracted = extract_passports(data)
    separated = [separate_fields(x) for x in extracted]
    valid = 0
    for passport in separated:
        if len(passport):
            valid += int(validate_passport_field_values(passport))
    return valid


def get_fields(pp):
    temp = []
    for field in pp:
        temp.append(field.split(':')[0])
    return temp


def get_fields_and_values(pp):
    fields = {}
    for field in pp:
        f_v = field.split(':')
        fields[f_v[0]] = f_v[1]
    return fields


def validate_passport_fields(passport):
    passport_fields = get_fields(passport)
    for field in required:
        if field not in passport_fields:
            return False
    else:
        return True


def validate_passport_field_values(passport):
    passport_fields = get_fields_and_values(passport)
    for field in required:
        if (field not in passport_fields.keys() or not(
            validate_field_value(field, passport_fields[field])
        )):
            return False
    return True


def validate_field_value(field, value):
    options = {
       'byr': validate_year,
       'iyr': validate_issue,
       'eyr': validate_expiration,
       'hgt': validate_height,
       'hcl': validate_hcolor,
       'ecl': validate_ecolor,
       'pid': validate_pid
    }
    valid = options[field](value)
    return valid


def validate_year(value):
    return len(value) == 4 and 1920 <= int(value) <= 2002


def validate_issue(value):
    return len(value) == 4 and 2010 <= int(value) <= 2020


def validate_expiration(value):
    return len(value) == 4 and 2020 <= int(value) <= 2030


def validate_height(value):
    if len(value) <= 2:
        return False
    h_val = int(value[:-2])
    if value[-2:] == 'cm':
        return 150 <= h_val <= 193
    elif value[-2:] == 'in':
        return 59 <= h_val <= 76
    else:
        return False


def validate_hcolor(value):
    if value[0] == '#' and len(value) == 7:
        try:
            int(value[1:7], 16)
            return True
        except ValueError:
            return False
    return False


def validate_ecolor(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_pid(value):
    try:
        int(value)
        return len(value) == 9
    except ValueError:
        return False


# RUNNER
def runner(path):
    with open(path, 'r') as f:
        print(validate_passports(f.read().split('\n')))


runner('./data')
