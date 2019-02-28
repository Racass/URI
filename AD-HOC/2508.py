myDic ={
    "A": 1, "J": 1, "S": 1,
    "B": 2, "K": 2, "T": 2,
    "C": 3, "L": 3, "U": 3,
    "D": 4, "M": 4, "V": 4,
    "E": 5, "N": 5, "W": 5,
    "F": 6, "O": 6, "X": 6,
    "G": 7, "P": 7, "Y": 7,
    "H": 8, "Q": 8, "Z": 8,
    "I": 9, "R": 9
}
myList = []
while(True):
    try:
        name = input()
        if(name == "" or name == "EoF"):
            break
        tempResultado = 0

        for char in name:
            if(myDic.__contains__(char.upper())):
                tempResultado += myDic[char.upper()]

        resultado = 0
        while(True):
            resultado = 0
            for char in str(tempResultado):
                resultado += int(char)
            tempResultado = resultado
            if(len(str(resultado)) == 1):
                break

        myList.append(resultado)
    except EOFError:
        break
for st in myList:
    print(st)
