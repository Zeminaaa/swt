# Spočítej faktoriál čísla N pomocí cyklu for. Faktoriál se počítá tak, že například faktoriál pěti je 5! = 5x4x3x2x1  nebo faktoriál osmi 8! = 8x7x6x5x4x3x2x1  
num=int(input("Zadej číslo: "))
p=[]
vysledek=1

for i in range(num):
    p.append(num)
    num-=1

for cislo in p:
    vysledek*=cislo    

print(vysledek)