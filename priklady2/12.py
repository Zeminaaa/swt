#12. Výběr studentů na základě průměru známek 

#Mějte stejnou strukturu jako v předchozím příkladu: 

studenti = {"Anna": "001", "Petr": "002", "Lucie": "003"} 

znamky = {"001": [1, 2, 1], "002": [3, 4, 5], "003": [1, 1, 2]} 

#Napište funkci, která: 
#Spočítá průměrnou známku každého studenta. 
#Vybere studenty s průměrnou známkou menší než 2.0. 

#Vrátí seznam jmen těchto studentů. 

#Rozšíření: Přidejte do výsledku také jejich ID a průměrnou známku ve formátu: 

#[("Anna", "001", 1.33), ("Lucie", "003", 1.33)] 

final_list=[]
for jmeno,idcko in studenti.items():
    if sum(znamky[idcko])/len(znamky[idcko])<2:
        final_list.append((jmeno,idcko,sum(znamky[idcko])/len(znamky[idcko])))
print(final_list)