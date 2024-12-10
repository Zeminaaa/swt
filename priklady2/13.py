#13. Pokročilá analýza a zpracování dat 

#Mějte následující data: 

studenti = {"Anna": {"id": "001", "vek": 15}, "Petr": {"id": "002", "vek": 16}, "Lucie": {"id": "003", "vek": 14}} 

znamky = {"001": [1, 2, 1], "002": [3, 4, 5], "003": [1, 1, 2]} 

#Napište funkci, která: 

#Spočítá průměrné známky studentů. 

#Vrátí nový slovník, kde klíčem bude věk studenta a hodnotou seznam jmen studentů s tímto věkem a jejich průměrnými známkami. 
#Výstupní formát: 

#{15: [("Anna", 1.33)], 16: [("Petr", 4.00)], 14: [("Lucie", 1.33)]} 

#Rozšíření: Pokud student nemá žádné známky, přiřaďte mu zprávu "Bez známek" místo průměru. 

final_list={}

posun=0

for jmeno,info in studenti.items():
    if len(znamky[info["id"]])>0:
        average=(sum(znamky[info["id"]])/len(znamky[info["id"]]))
    else:
        average="Bez známek"
    if info["vek"] not in  final_list:
        final_list[info["vek"]]=[]

    final_list[info["vek"]].append((jmeno,average))
    
print(final_list)
