import math 
n = int(input())

myDic = {
    "Coelho": 0,
    "Rato": 0,
    "Sapo": 0
}

for x in range(0, n):
    inp = input()
    if("C" in inp): #Coelho
        myDic["Coelho"] += int(inp.replace(" C", "")) 
    elif("R" in inp): #Rato
        myDic["Rato"] += int(inp.replace(" R", "")) 
    elif("S" in inp): #Sapo
        myDic["Sapo"] += int(inp.replace(" S", "")) 

myResult = {
    "Total": 0,
    "Total_coelho": 0,
    "Total_rato": 0,
    "Total_sapo": 0,
    "Perc_coelho": 0.00,
    "Perc_rato": 0.00,
    "Perc_sapo": 0.00
}

for key in myDic:
    myResult["Total"] += myDic[key]

myResult["Total_coelho"] = myDic["Coelho"]
myResult["Total_rato"] = myDic["Rato"]
myResult["Total_sapo"] = myDic["Sapo"]

myResult["Perc_coelho"] = (100 * myDic["Coelho"]) / myResult["Total"]
myResult["Perc_rato"] = (100 * myDic["Rato"]) / myResult["Total"]
myResult["Perc_sapo"] = (100 * myDic["Sapo"]) / myResult["Total"]

print("Total: " + str(myResult["Total"]) + " cobaias")
print("Total de coelhos: " + str(myResult["Total_coelho"]))
print("Total de ratos: " + str(myResult["Total_rato"]))
print("Total de sapos: " + str(myResult["Total_sapo"]))
print("Percentual de coelhos: " + "{0:.2f}".format(round(myResult["Perc_coelho"], 2)) + " %")
print("Percentual de ratos: " + "{0:.2f}".format(round(myResult["Perc_rato"], 2)) + " %")
print("Percentual de sapos: " + "{0:.2f}".format(round(myResult["Perc_sapo"], 2)) + " %")