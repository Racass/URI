n = int(input())

myList = []


for x in range(n):
    myList.append(int(input()))
myRes = []
for number in myList:
    if((number > 0) and (number % 2 == 0)):  #POSITIVO + PAR
        myRes.append("EVEN POSITIVE")
    elif((number < 0) and (number % 2 == 0)): #NEGATIVO + PAR
        myRes.append("EVEN NEGATIVE")
    elif(((number > 0) and (number % 2 != 0))):#POSITIVO + IMPAR
        myRes.append("ODD POSITIVE")
    elif((number < 0) and (number % 2 != 0)): #NEGATIVO + IMPAR
        myRes.append("ODD NEGATIVE")
    elif(number == 0):
        myRes.append("NULL")

for string in myRes:    
    print(string)