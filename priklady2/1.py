#1. Základy seznamů 
#
#Napište program, který vytvoří seznam čísel od 1 do 10 a vytiskne každé číslo na nový řádek.

p=[]
num=1
for i in range(10):
    p.append(num)
    print(num)
    num+=1
