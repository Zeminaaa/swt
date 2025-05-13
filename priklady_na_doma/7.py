num10=int(input("Zadej číslo v desítkové soustavě: "))
vysledek=""
while(num10>0):
    zbytek=num10%2
    vysledek=str(zbytek)+vysledek
    num10=num10//2
print(f"Vaše číslo je v binární soustavě: {vysledek}")