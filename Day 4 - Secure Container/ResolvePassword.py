def CheckStringDuplicate(num):
    for c in num:
        if num.count(c) > 1:
            return True
    return False

def CreateIntegerListBewteenRanges(start, end):
    return list(range(start,end))

def CreateIntegerStingListFromIntgers(integers):
    return [ str(num) for num in integers ]

def DoesIntegerContainZero(integer):
    if '0' in (str(integer)):
        return True
    else:
        return False

def FilterIntegresWithZero(integers):
    return [ num for num in integers if DoesIntegerContainZero(num) == False ]

def IsFollingIntegerGreaterOrEqualThanCurrent(current, following):
    if following >= current:
        return True
    else:
        return False

def TransformIntegerToList(integer):
    return list(map(int,str(integer)))

def ProcessIntegerForAcendingNumbers(integer):
    numbersInInteger = TransformIntegerToList(integer)
    for index in range(0, len(numbersInInteger) - 1):
        if IsFollingIntegerGreaterOrEqualThanCurrent(numbersInInteger[index], numbersInInteger[index + 1]) == False:
            return False

    return True

def FilterAcendingIntegerSequence(integers):
    acendingIntegerFilter = []
    for integer in integers:
        if ProcessIntegerForAcendingNumbers(integer):
            acendingIntegerFilter.append(integer)
    return acendingIntegerFilter

def FilterDuplicateIntegers(integers):
    integersWithDuplicates = []
    for integer in integers:
        if CheckStringDuplicate(str(integer)):
            integersWithDuplicates.append(integer)
    return integersWithDuplicates

if __name__ == "__main__":
    integers = CreateIntegerListBewteenRanges(254032,789860)
    #integersAsStrings = CreateIntegerStingListFromIntgers(integers)
    #integersWithoutZeros = FilterIntegresWithZero(integers)
    integersWithAcendingOrder = FilterAcendingIntegerSequence(integers)
    integersWithDuplicates = FilterDuplicateIntegers(integersWithAcendingOrder)
    
    
    print("Integers Length: {}\nIntegers With Acending Order: {}\nIntegers With Duplicates: {}".format(len(integers),len(integersWithAcendingOrder),len(integersWithDuplicates)))
    pass