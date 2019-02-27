i = 0
j = 1

j_init = 1

while(i <= 2):
    if(j > j_init + 2):
        i += 0.2
        j = j_init + 0.2
        j_init = j
    if(i > 2):
        break
    print("I=" + "{:.1f}".format(i).replace(".0", "") + " J=" + "{:.1f}".format(j).replace(".0", ""))
    j += 1
    