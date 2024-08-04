"""
Question : https://www.hackerrank.com/challenges/nested-list/problem
Done
"""
def checkLowest(lowestStudent, isLowest):
    currentLowest = lowestStudent[0][1]
    return True if isLowest*1000 < currentLowest*1000 else False
def checkEqual(lowestStudent, isEqual):
    currentLowest = lowestStudent[0][1]
    return True if currentLowest == isEqual else False
def checkAlphabetOrder(secondLowest, appendingName, appendingScore):
    previousName = secondLowest[0][0]
    if previousName > appendingName:
        secondLowest[:0] = [[appendingName, appendingScore]]
    else:
        secondLowest.append([appendingName, appendingScore])
    return secondLowest
if __name__ == '__main__':
    secondLowest = list()
    Lowest = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if(len(Lowest)==0):
            Lowest.append([name, score])
        else:
            if(checkEqual(Lowest , score)):
                Lowest = checkAlphabetOrder(Lowest, name, score)
            elif(checkLowest(Lowest , score)):
                secondLowest = list(Lowest)
                Lowest = []
                Lowest.append([name, score])
            else:
                if(len(secondLowest)==0):
                    secondLowest.append([name, score])
                elif(checkLowest(secondLowest , score)):
                    secondLowest = []
                    secondLowest.append([name, score])
                elif(checkEqual(secondLowest , score)):
                    secondLowest = checkAlphabetOrder(secondLowest, name, score)
    for name,score in secondLowest:
        print(name)
            
