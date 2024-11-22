# Napište program, který vrátí nový řetězec, ve kterém bylo každé písmenko zdvojeno. 
text=input("zadej text: ")
p=[]
vysledek=""

for pismeno in text:
    p.append(pismeno)

for pismeno in p:
        vysledek+=(pismeno)
        vysledek+=(pismeno)
print(vysledek)       