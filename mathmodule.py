def factors(number):
    output = []
    for i in range(1 , number + 1):
        if number % i == 0:
            output.append(i)
    return(output)

def isprime(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    if (len(factors) == 2):
        if factors[0] == 1 and factors[1] == number:
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
    for i in range(int(round(number)) + 2):
        if i >= number:
            return(i)

def floor(number):
  if isinstance(number, int):
    return int(number)
  else:
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

RToDRatio = 180 / piconstant
def degrees(radians):
    return(RToDRatio * radians)

DToRRatio = piconstant / 180
def radians(degrees):
    return(DToRRatio * degrees)
