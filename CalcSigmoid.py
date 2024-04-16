import csv

from Sigmoid import Sigmoid


def calcSigmoid(num: int):

    sigmoid = Sigmoid(num)
    print("Sigmoid of ", num, " = ", sigmoid.calculate())
    return


def readFile(filePath: str):
    csvReader = csv.reader(open(filePath, 'r+'))

    for row in csvReader:
        print("Row: {}".format(row))

calcSigmoid(1)
readFile("my_data.csv")

