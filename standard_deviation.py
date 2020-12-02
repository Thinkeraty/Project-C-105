import math
import csv

with open('class2.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)

data = file_data[0]

def find_mean(data):
    n = len(data)
    total = 0

    for i in data:
        total+=int(i)
    
    mean = total/n
    return mean

square = []

for x in data:
    a = int(x) - find_mean(data)
    a = a**2
    square.append(a)

sum = 0

for j in square:
    sum += j

result = sum/(len(data) - 1)

deviation = math.sqrt(result)

print(deviation)