# Spočítej faktoriál čísla N pomocí cyklu while. 
num=int(input("Zadej číslo: "))
vysledek=1

while True:
    vysledek*=num
    if num==1:
        break
    num-=1
print(vysledek)