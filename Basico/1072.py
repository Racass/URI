n = int(input())
myList = []
for x in range(0, n):
    myList.append(int(input()))
in_list = 0
out_list = 0
for y in myList:
    if(y >= 10 and y <= 20):
        in_list += 1
    else:
        out_list += 1

print(str(in_list) + " in" )
print(str(out_list) + " out" )