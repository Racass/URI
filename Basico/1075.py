n = int(input())

myList = [] 
for number in range(1, 10000):
    if(number % n == 2):
        myList.append(number)

for string in myList:
    print(string)
