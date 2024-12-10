#7. Najdi nejvyšší průměr 

#Použijte slovník ze cvičení č. 6. 
#Napište funkci, která vrátí jméno studenta s nejvyšším průměrem známek. 

znamky = {"Anna": [1, 2, 3], "Petr": [3, 4, 5], "Lucie": [2, 2, 3]} 


maxprumer=0
jmeno=None
for student in znamky:
    prumer=sum(znamky[student])/len(znamky[student])
    if prumer>maxprumer:
        maxprumer=prumer
        jmeno=student

print(f"{jmeno} měl největší průměr: {maxprumer}")
