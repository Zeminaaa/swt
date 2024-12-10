#6. Průměr známek ve slovníku 
#Vytvořte slovník obsahující studenty a jejich známky: 

znamky = {"Anna": [1, 2, 3], "Petr": [3, 4, 5], "Lucie": [2, 2, 3]} 

#Napište funkci, která spočítá a vrátí průměr známek pro každého studenta. 
for student in znamky:
    print(f"{student}: {sum(znamky[student])/len(znamky[student])}")