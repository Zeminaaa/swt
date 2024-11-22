# Napiš program, který načte ze vstupu textový řetězec obsahující číslo (například „568“) a převede ho na proměnnou typu int.
# Nesmíš využít funkci int(). Představ si, že jsi člověk, který ji programuje. Můžeš například využít ascii tabulku a funkci ord(). 
string=str(input("zadej číslo: "))
delka=len(string)
p=[]
ascii_list=[]
posun=0
vysledek=0
for charakter in string:
    p.append(charakter)

for charakter in p:
    temp=ord(charakter)
    ascii_list.append(temp)

for i in range(delka):
    temp=float(chr(ascii_list[0+posun]))
    vysledek+=(10**(delka-1))*temp
    posun+=1
    delka-=1
vysledek=round(vysledek)
print(vysledek)


# asi to nejde, na řádku 17 mám error, protože ascii tabulka vrací ve formě stringu a ne integeru.
# když se místo float tam dá int tak to funguje, ale to nemůžu správně. bez toho to nefunguje protože mi nechce počítat se stringem.