def CheckStringDuplicate(num):
    for c in num:
        if num.count(c) > 1 and (num.count(c) % 2) == 0:
            return True
    return False


if __name__ == "__main__":
    holeNumbers = list(range(254032,789860,1))
    holeNumbersAsStrings = [ str(num) for num in holeNumbers]
    zeroFilter = [ num for num in holeNumbersAsStrings if('0' in num) == False ]
    increasFilter = zeroFilter.copy()
    hasDuplicate = []
    for num in zeroFilter:
        for index in range(0,len(num)-1):
            if int(num[index + 1]) < int(num[index]):
                increasFilter.remove(num)
                break
    for num in increasFilter:
        if(CheckStringDuplicate(num)):
            hasDuplicate.append(num)
    print("lastFilter: {}".format(hasDuplicate))
    print("Guesses Length: {}\nnoZeros Length: {},\nincreaseFilter: {}\nhasDuplicates: {}".format(len(holeNumbersAsStrings), len(zeroFilter),len(increasFilter),len(hasDuplicate)))
    pass