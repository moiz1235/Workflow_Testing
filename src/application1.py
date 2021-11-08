def getExponential(a, b):
    return (a ** b)
#Demo comment

def testGreaterThan10(x):
    if x > 10 and x != 10:
        return True
    elif x < 10 and x != 10:
        return False
    elif x == 10:
        return None


def getSquared(a):
    list = []
    for element in a:
        list.append(element**2)
    return list

getSquared([1,2])
testGreaterThan10(9)
getExponential(2,3)