cisloB=input("Zadej číslo v dvojkové soustavě: ")
lenght= len(cisloB)
cislo10=0
mocnina=1
for i in range(lenght):
    part=int(cisloB[lenght-1])
    lenght-=1
    cislo10+=int(part*mocnina)
    if mocnina>1:
        mocnina*=2
    if mocnina==1:
        mocnina=2
print(f"Číslo {cisloB} je v desítkové soustavě {cislo10}.")