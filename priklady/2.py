# Napište program, který vypíše tabulku mocnin dle následujícího zadání. Počet prvků budiž parametrický. 
p=[]
pocet=int(input("do jakého čísla chceš tabulku?: "))
pocet_mocnin=int(input("kolikrát chceš umocňovat na duhou?: "))
nasobitel=1

for temp in range(pocet):
    temp=nasobitel
    p.append(temp)
    nasobitel+=1


print(f"{p}\n{nasobitel*"- "}")

for num in p:
    print(f"{num} | ", end="")
    nasobitel=1
    for i in range(pocet_mocnin):
        print(f"{num**nasobitel} ", end="")
        nasobitel+=1
    print("")
