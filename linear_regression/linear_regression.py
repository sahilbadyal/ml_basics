'''
This code implements basic linear regression using scaler weights. This is capable of learning linear functions like

y = x + 2

'''
import csv
import random

datatuple = []

#this dataSetTest has been generated using create_data_set_linear_fn.py
with open('dataSetTest.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        datatuple.append((row[0],row[1]))

#initializing a and b randomly These are the weights which will be learnt by the model

a = random.randint(-1000,1000)
b = random.randint(-1000,1000)
#print (a,b)
alpha = 0.01 #learning rate

for dtuple in datatuple:
    actx = float(dtuple[0])
    acty = float(dtuple[1])
    y = a*actx + b
    delY = acty - y
    #Using stochastic gradient descent algorithm here for optimization of loss (delY)
    delA = -(delY/actx)
    delB = -delY
    a = a - alpha*delA
    b = b - alpha*delB


##Test to evaluate the model
x = input("Number")
x= int(x)
print(int(a*x+b))
print (a,b)

