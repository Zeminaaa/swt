#10.Pokročilé zpracování dat 

#Mějte slovník se jmény studentů a jejich známkami: 

znamky = {"Anna": [1, 1, 2], "Petr": [3, 4, 5], "Lucie": [2, 2, 3], "Jan": []} 

#Napište funkci, která: 
#Spočítá průměrné známky studentů, pokud mají nějaké známky. 
#Studentům bez známek přiřadí zprávu "Bez známek". 
#Vrátí nový slovník, kde jsou klíčem jména studentů a hodnotou buď průměrná známka, nebo zpráva. 

for student, aspon_neco in znamky.items():
    if aspon_neco:
        znamky[student]=sum(znamky[student])/len(znamky[student])
    else:
        znamky[student]="Beze známek"
print(znamky)
