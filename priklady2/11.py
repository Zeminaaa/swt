#11. Spojení dat z více slovníků 

#Mějte následující struktury: 

studenti = {"Anna": "001", "Petr": "002", "Lucie": "003"} 

znamky = {"001": [1, 2, 1], "002": [3, 4, 5], "003": [1, 1, 2]} 

#napište funkci, která: 
#Zkombinuje informace o studentech a jejich známkách do nového slovníku ve formátu: 

#{"Anna": [1, 2, 1], "Petr": [3, 4, 5], "Lucie": [1, 1, 2]} 

for jmeno,idcko in studenti.items():
    studenti[jmeno  ]=znamky[idcko]

print(studenti)
