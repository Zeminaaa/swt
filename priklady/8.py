# Napište program, který počítá největší společný dělitel čísel a a b. Může pracovat naivně, tj. zkoušet všechny možnosti a podobně. 
num1=int(input("zadej první číslo: "))
num2=int(input("zadej druhé číslo: "))
if num2>num1:
    temp=num1
    num1=num2
    num2=temp
while True:
    zbytek=num1-(int(num1/num2)*num2)
    num1=num2
    num2=zbytek
    if zbytek==0:
        break
print(f"\n{num1} je největší společný dělitel zadaných čísel")

# na tohle jsem bohužel nepřišel, tak jsem program udělal podle wiki: https://cs.wikipedia.org/wiki/Eukleid%C5%AFv_algoritmus#Uk%C3%A1zka_%C4%8Dinnosti_algoritmu