# Napiš program, který načte ze vstupu textový řetězec obsahující číslo (například „568“) a převede ho na proměnnou typu int.
# Nesmíš využít funkci int(). Představ si, že jsi člověk, který ji programuje. Můžeš například využít ascii tabulku a funkci ord(). 
zadani=str(input("zadej číslo: "))
delka=len(zadani)
p=[]
vysledek=0

p=list(zadani)

for charakter in p:
    temp=ord(charakter)
    vysledek+=(10**(delka-1))*(temp-48)
    delka-=1

print(vysledek)
