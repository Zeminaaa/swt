import random
MAPA_VYSKA=11
MAPA_SIRKA=11


POLICKO_PRAZDNE=0
POLICKO_ZED=1
POLICKO_SEED=2
POLICKO_HRAC=3
POLICKO_ENEMY=4
POLICKO_COIN=5

def generuj_pole():
    mapa=[]
    for i in range(MAPA_VYSKA):
        temp=[]
        for i in range(MAPA_SIRKA):
            temp.append(POLICKO_PRAZDNE)
        mapa.append(temp)
    return mapa

def vytiskni_pole(mapa):
    for radek in mapa:
        print(radek)

def vytvor_okraj(mapa):
    for y in range(MAPA_VYSKA):
        for x in range(MAPA_SIRKA):
            if x==0 or y==0 or x==MAPA_SIRKA-1 or y==MAPA_VYSKA-1:
                mapa[y][x]=POLICKO_ZED

def vytvor_seedy(mapa):
    for y in range(2,MAPA_VYSKA-2,2):
        for x in range(2,MAPA_SIRKA-2,2):
                mapa[y][x]=POLICKO_SEED




bludiste = generuj_pole()
vytvor_okraj(bludiste)
vytvor_seedy(bludiste)
vytiskni_pole(bludiste)


pocet_seedu=0
for radek in bludiste:
    for seed in radek:
        if seed==POLICKO_SEED:
            pocet_seedu+=1

vybrany_seed=random.randint(0,pocet_seedu)
temp=0
x=-1
y=-1
for radek in bludiste:
    y+=1
    for seed in radek:
        x+=1
        if seed==POLICKO_SEED:
            pocet_seedu+=1
            if temp==pocet_seedu:
                print(bludiste[x][y])
