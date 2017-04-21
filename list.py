import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
nums = string.digits



def initialCheck(pass):
    return if not [x for x in pass if x in upper] \
        and if not [y for y in pass if y in lower] \
        and if not [z for z in pass if z in nums]

def strengthCheck(pass):
    if not initialCheck(pass):
        return 0

    a = 0.5
    b = 0.2
    c = 1 - a - b

    special = [x for x in pass if x not in upper or\
     x not in lower\
     x not in nums]

    return int(a * len(pass)\
        + b )
