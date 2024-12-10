#5. Počet výskytů hodnoty 
#Napište program, který spočítá, kolikrát se hodnota "Python" vyskytuje v seznamu: 

kurzy = ["Python", "Java", "Python", "C++", "Python"] 

total=0
for text in kurzy:
    if text=="Python":
        total+=1
print(f"počet hodnot je: {total}")