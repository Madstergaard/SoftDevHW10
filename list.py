import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
nums = string.digits



def initialCheck( pswd ):
    return  [x for x in pswd if x in upper] \
        and [y for y in pswd if y in lower] \
        and [z for z in pswd if z in nums]

def strengthCheck(pswd):
    if not initialCheck(pswd):
        return 0

    a = 0.5
    b = 0.2
    c = 0.3

    retNum = [0.6 for x in pswd if x in upper]
    retNum += [0.4 for y in pswd if y in lower]
    retNum += [1 for z in pswd if z in nums]
    
    special = [x for x in pswd if x not in upper or\
     x not in lower or \
     x not in nums]

    ctr = 0
    for x in retNum:
        ctr += x
    
    return ctr



print strengthCheck("abcABC123#")
