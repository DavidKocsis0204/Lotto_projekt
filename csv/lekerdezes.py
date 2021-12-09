import csv

with open('H:\Python\otos.csv', 'r') as file:
    reader = csv.reader(file)
    tomb=[]
    line=0
    for row in reader:
        if  line==0:
            continue
        tomb.append(row)
#Beolvasás--------------------------
    sro=str(tomb[1]).split(';')
    print(sro[11:16])
#Lekérdezés_1-----------------------
    sro_ketto=str(tomb[2]).split(;)
    print(sro_ketto[11:16])