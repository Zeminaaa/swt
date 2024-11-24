# Napiš program, který načte ze vstupu textový řetězec obsahující číslo (například „568“) a převede ho na proměnnou typu int.
# Nesmíš využít funkci int(). Představ si, že jsi člověk, který ji programuje. Můžeš například využít ascii tabulku a funkci ord(). 
zadani=str(input("zadej číslo: "))
delka=len(zadani)
p=[]
p_int=[]
posun=0
vysledek=0

p=list(zadani)

for charakter in p:
    temp=ord(charakter)
    p_int.append(temp-48)

for i in range(delka):
    vysledek+=(10**(delka-1))*(p_int[posun])
    posun+=1
    delka-=1

print(vysledek)
