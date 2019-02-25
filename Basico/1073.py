N = int(input())
myList = []
for x in range(N+1):
    if(x % 2 == 0 and x > 0):
        myList.append(str(x) + "^2 = " + str(x**2))

for res in myList:
    print(res)
