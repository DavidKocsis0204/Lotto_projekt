import csv

with open('H:\Python\otos.csv', 'r') as file:
    reader = csv.reader(file)
    tomb=[]
    for row in reader:
        tomb.append(row)
#print(tomb)
    print(tomb[1])

tomb_two=[[1,6,7][1,2,3,4]]
print(tomb_two[1][2])    

