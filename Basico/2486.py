myDic = {
    "suco de laranja": 120,
    "morango fresco": 85,
    "mamao": 85,
    "goiaba vermelha": 70,
    "manga": 56,
    "laranja": 50,
    "brocolis": 34
}
 
tempResult  = []
myResult    = []

while(True):
    t = int(input())
    if(t == 0):
        break
    tempDic = {}
    for number in range(0, t):
        take = input().split(' ')
        if(len(take) == 2):
            tempDic[take[1]] = int(take[0])
        elif(len(take) == 4):
            tempDic[take[1] + " " + take[2] + " " + take[3]] = int(take[0])
        elif(len(take) == 3):
            tempDic[take[1] + " " + take[2]] = int(take[0])
    for orig in myDic:
        for new in tempDic:
            if(new == orig):
                tempResult.append(int(myDic[orig]) * int(tempDic[new]))
    result = 0
    for number in tempResult:
        result += number
    if(result > 130):
        myResult.append("Menos " + str(result - 130) + " mg")
    elif(result < 110):
        myResult.append("Mais " + str(110 - result) + " mg")
    else:
        myResult.append(str(result) + " mg")
    tempDic.clear()
    tempResult.clear()

for st in myResult:
    print(st)