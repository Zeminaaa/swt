#8. Základní analýza dat 

#Mějte seznam věků: 

veky = [12, 15, 17, 12, 16, 15, 15, 16] 

#Napište funkci, která: 
#Vrátí nejčastější věk v seznamu. 
#Spočítá počet unikátních věků. 
p={}
for vek in veky:
    if vek not in p:
        p[vek]=1
    else:
        p[vek]+=1

print(f"Počet unikátních věků je: {len(p)}")

total=0
nejcastejsi=None
for vek in p:
    if p[vek]>total:
        total=p[vek]
        nejcastejsi=vek

print(f"Nejčastější věk je: {nejcastejsi}")