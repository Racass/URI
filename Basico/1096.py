i = 1
j = 8

while(True):
    if(j <= 5):
        i += 2
        j = 8
    j -= 1
    print("I=" + str(i) + " J=" + str(j))
    if(i == 9 and j == 5):
        break