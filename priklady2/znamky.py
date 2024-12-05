p={}

studenti = {
    "Anna": {"id": "001", "vek": 15},
    "Petr": {"id": "002", "vek": 16},
    "Lucie": {"id": "003", "vek": 16}
 }

znamky = {
    "001": [1, 2, 1],
    "002": [3, 4, 5],
    "003": [1, 1, 2]
    }

posun=0

for jmeno,info in studenti.items():
    

        

    test=(znamky[info["id"]])
    znamka=(sum(test)/len(test))


    vek=info["vek"]
 
    

    if info["vek"] not in  p:
        
        p[info["vek"]]=[]

    p[info["vek"]].append((jmeno,znamka))
    
    




print(p)
