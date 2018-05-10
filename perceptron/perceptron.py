'''
This is the basic implementation of perceptron which learns or operation
'''
import sys
import time
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def delete_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

def matmul(a,b):
   return a[0]*b[0] + a[1]*b[1]

def add(a,b):
    return [a[0]+b[0], a[1]+b[1]]

dataSet  = [False,True]

W = [0.0,0.0]
b = 0

def predict(inp):
    global W,b
    out = matmul(W,inp) + b
    Y  = 1 if out > 0 else 0
    return Y

def train(inp,out):
    global W,b
    Y = predict(inp)
    #print (inp,Y,W,b)
    #print ("Out=",out)
    delY =  out - Y
    delW = [delY * x for x in inp]
    #print ("delW",delW)
    W  =  add(W,delW)
    b += delY
    return delY

def run(function):
    loss = 4
    epoc = 0
    while loss is not 0:
        loss = 0
        for value in dataSet:
            for value2 in dataSet.copy():
                INP = [int(value),int(value2)]
                #print("INP = ",INP)
                OR  = int(value | value2)
                AND = int(value & value2)
                XOR = int(value ^ value2)
                if (function=="OR"):
                    ACT = int(OR)
                elif (function=="AND"):
                    ACT = int(AND)
                else:
                    ACT = int(XOR)
                #print("ACT =", ACT)
                loss += abs(train(INP,ACT))
        epoc += 1
        print("Loss after epoc %d = %d"%(epoc,loss))



#train network

func   = input("Function to implement\n1. OR \n2. AND\n3.XOR (This cannot be classified by a single layer perceptron)==> ")
#nEpocs = input("Number of epocs: ")

if (func=='1'):
    run('OR')
elif (func=='2'):
    run('AND')
else:
    print("Trying to train XOR which is not possible by perceptron, Press crtl +C to stop epocs")
    run('XOR')


#test time
print ("Crtl+C is used to Quit")

while True:
    x = input("Number1: ")
    y = input("Number2: ")
    INP = [int(x),int(y)]
    OUT = predict(INP)
    print("Output = ",OUT)
    time.sleep(1)
    delete_last_lines(3)
