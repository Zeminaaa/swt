with open("data.txt","r") as soubor:
    data=soubor.readline()

list_of_nums=["0","1","2","3","4","5","6","7","8","9"]
cisla=[]
temp=""

for znak in data:
    if znak in list_of_nums:
        temp+=znak
    else:
        if temp!="":
            cisla.append(temp)
        temp=""

dmez=int(input("Zadej dolní mez intervalu: "))
hmez=int(input("Zadej horní mez intervalu: "))

vysledek=[]
suma=0

for cislo in cisla:
    if int(cislo) >= dmez and int(cislo) <= hmez:
        vysledek.append(cislo)
        suma+=1
    
print("\nČísla ležící v zadaném intervalu")
for cislo in vysledek:
    print(cislo,end=" ")
print(f"\nPočet čísel v intervalu {dmez} až {hmez} = {suma}")