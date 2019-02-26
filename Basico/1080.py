big = -40000000000000
pos = 0
for n in range(1, 101):
    x = int(input())
    if(x > big):
        big = x
        pos = n

print(big)
print(pos)