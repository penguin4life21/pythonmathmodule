def factors(number):
    output = []
    for i in range(1 , number + 1):
        if number % i == 0:
            output.append(i)
    return(output)

def isprime(number):
    factorslist = factors(number)
    if (len(factorslist) == 2):
        if factorslist[0] == 1 and factorslist[1] == number:
            return(True)
        else:
            return(False)
    else:
        return(False)

def mean(List):
    return(sum(List) / float(len(List)))

def median(List):
    sortedList = sorted(List)
    ListLen = len(List)
    index = (ListLen - 1) // 2   
    if (ListLen % 2):
        return sortedList[index]
    else:
        return (sortedList[index] + sortedList[index + 1])/2.0
    
def mode(List):
    return(max(set(List), key=List.count))

def ceil(number):
    if float(int(number)) == number:
        return float(number)
    else:
        return float(int(number))+1

def floor(number):
    return float(int(number))

def ispositive(number):
    if number < 0:
        return False
    else:
        return True

def isnegative(number):
    if number >= 0:
        return False
    else:
        return True

def nthrt(number, root):
    return(number ** float(root ** -1))

def sqrt(number):
    return(number ** 0.5)

pi = float(open("pi.txt", "r").read())

def pi(length=0):
    if length == 0:
        pifile = open("pi.txt", "r")
        return float(pifile.read())
    else:
        pifile = open("pi.txt", "r")
        return float(pifile.read()[0:(length+2)])

RToDRatio = 180 / pi(10)
def degrees(radians):
    return(RToDRatio * radians)

DToRRatio = pi(180) / 180
def radians(degrees):
    return(DToRRatio * degrees)

def binary(decimal):
    unformatted = bin(decimal)
    return(int(unformatted[2:]))
