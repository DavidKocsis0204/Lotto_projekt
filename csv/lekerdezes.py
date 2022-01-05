import csv
from os import system

system('cls')

with open('D:\GitKd\Lotto_projekt\csv\otos.csv', 'r') as file:
    reader = csv.reader(file)
    tomb=[]
    line=0
    for row in reader:
        if  line==0:
            line=line+1
            continue
        else:
            line=line+1
            #print(row)
            line_tomb=[]
            line_tomb.append(row[0].split(';')[11:16])
            #print(line_tomb) 
            tomb.append(line_tomb)
    #teszteléshez
    #print(tomb[0])

#Beolvasás--------------------------
    sor_elso=[]
    sor_elso.append(tomb[0][0][0:5])
    print(sor_elso)
#Lekérdezés_1-----------------------
    sor_masodik=[]
    sor_masodik.append(tomb[1][0][0:5])
    print(sor_masodik)
#lekérdezés_2-----------------------
    lottoszamok=[]
    
    leggyakoribb=[]
    for i in range(1,100):
        leggyakoribb.append(i)
    lottoszamok.append(leggyakoribb)
    
    db=[]
    for i in leggyakoribb:
        db.append(0)
    lottoszamok.append(db)
    
    for i in range(1,100):
        for j in range(5):
            tomb[i][0][0:5] #befejezetlen
            
    #print(lottoszamok)