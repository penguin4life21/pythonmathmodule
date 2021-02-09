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
    for i in range(int(round(number)) + 2):
        if i >= number:
            return(i - 1)

def ispositive(number):
    string = str(number)
    if (string[0] != "-"):
        return(True)
    else:
        return(False)

def isnegative(number):
    string = str(number)
    if (string[0] == "-"):
        return(True)
    else:
        return(False)





    

