n = int(input())
myList = []
finalList = [] 

for number in range(0, n):
    tempList = []
    a,b,c = input().split(" ")
    tempList.append(float(a))
    tempList.append(float(b))
    tempList.append(float(c))
    myList.append(tempList)

for temp in myList:
    x = temp[0] * 2 + temp[1] * 3 + temp[2] * 5
    x = x / 10
    finalList.append(x)


for number in finalList:
    print('{:.1f}'.format(number))

