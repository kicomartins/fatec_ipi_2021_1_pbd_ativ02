#URI 1001

n1 = int(input())
n2 = int(input())
soma = (n1+n2)
print("X =" ,soma)

#URI 1015

import math

linha1 = input().split(" ")
linha2 = input().split(" ")

x1,y1 = linha1
x2,y2 = linha2

distancia = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))

print("%0.4f" %distancia)

#URI 1078

n = int(input())

for i in range(1, 11):
    print('{} x {} = {}'.format(i , n , i * n))

#URI 1069

T = int(input())
while T>0:
    Str = input()
    Count = 0
    Sign = 0
    for i in Str:
        if (i == "<"):
            Sign += 1
        if (i == ">" and Sign > 0):
            Count += 1
            Sign -= 1
    print(Count)
    T-=1