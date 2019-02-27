def getImparConsec(x, y):
    resultado = 0
    if(x > y):
        while(True):
            x -= 1
            if(x <= y):
                break
            if(x % 2 != 0):
                resultado += x    
    if(x < y):
        while(True):
            x += 1
            if(x >= y):
                break
            if(x % 2 != 0):
                resultado += x
    return resultado

n = int(input())

myList = []

for number in range(0, n):
    myList.append(input())

myResult = []

for n in myList:
    x = n.split(' ')
    myResult.append(getImparConsec(int(x[0]), int(x[1])))

for st in myResult:
    print(st)
