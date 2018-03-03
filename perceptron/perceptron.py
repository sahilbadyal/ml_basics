import csv
import random

datatuple = []

with open('dataSetTest.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        datatuple.append((row[0],row[1]))

a = random.randint(-1000,1000)
b = random.randint(-1000,1000)
print (a,b)
alpha = 0.01

for dtuple in datatuple:
    actx = float(dtuple[0])
    acty = float(dtuple[1])
    y = a*actx + b
    delY = acty - y
    delA = -(delY/actx)
    delB = -delY
    a = a - alpha*delA
    b = b - alpha*delB

x = input("Number")
x= int(x)
print(int(a*x+b))
print (a,b)

