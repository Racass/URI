i = 1
j = 8

i_init = 1
j_init = 8

while(True):
    if(j <= (j_init - 3)):
        i += 2
        j = j_init + 2
        j_init = j
    j -= 1
    print("I=" + str(i) + " J=" + str(j))
    if(i ==  9 and j == 13):
        break