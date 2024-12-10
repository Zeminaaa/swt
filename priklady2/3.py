#3. Přístup k hodnotám ve slovníku 
#Mějte slovník: 
#studenti = {"Anna": 15, "Petr": 16, "Lucie": 14} 
#Vytiskněte jména všech studentů, kteří mají věk větší než 15. 

studenti = {"Anna": 15, "Petr": 16, "Lucie": 14} 
for student in studenti:
    if studenti[student]>15:
        print(student)