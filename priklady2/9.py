#9. Filtr studentů podle věku 

#Mějte slovník studentů a jejich věků: 

studenti = {"Anna": 15, "Petr": 16, "Lucie": 14, "Jan": 17} 

#Napište funkci, která vrátí jména všech studentů starších než 15 let. 

for student in studenti:
    if studenti[student]>15:
        print(student)