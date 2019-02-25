x = int(input())
y = int(input())

resultado = 0

while(True):
    x -= 1
    if(x <= y):
        break
    if(x % 2 != 0):
        resultado += x

print(resultado)