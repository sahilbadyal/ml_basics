import csv
import random


def createDataset(fileName,length):
    with open(fileName+'.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        listOf = []
        for x in range(length):
            y = random.randint(-10000,10000)
            tuples = (y,y+2)
            listOf.append(tuples)
        writer.writerows(listOf)


createDataset('test',5000)
createDataset('train',50000)
