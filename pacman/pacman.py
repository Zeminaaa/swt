import random
import time
import os

MAPA_VYSKA=11
MAPA_SIRKA=11


POLICKO_PRAZDNE=0
POLICKO_ZED=1
POLICKO_SEED=2
POLICKO_HRAC=3
POLICKO_ENEMY=4
POLICKO_COIN=5

def generuj_pole(znak):
    mapa=[]
    for i in range(MAPA_VYSKA):
        temp=[]
        for i in range(MAPA_SIRKA):
            temp.append(znak)
        mapa.append(temp)
    return mapa

def vytiskni_pole(mapa):
    slovnik = {
  0: "  ",
  1: "# ",
  2: "* ",
  3: "P ",
  4: "E ",
  5: "$ "
}
    for radek in mapa:
        for znak in radek:
            print(slovnik[znak],end="")
        print("")

def vytiskni_pole_test(mapa):
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

def znic_seedy(mapa):
    y=-1
    x=-1
    for radek in bludiste:
        y+=1
        for policko in radek:
            x+=1
            if policko==POLICKO_SEED:
                roll=random.randint(0,1)
                if roll==1:
                    mapa[y][x]=POLICKO_ZED
        x=-1        

def vytvor_zdi(mapa):
    pocet_seedu=0
    for radek in bludiste:
        for seed in radek:
            if seed==POLICKO_SEED:
                pocet_seedu+=1

    check=True
    while check:
       
        vybrany_seed=random.randint(0,pocet_seedu)  
        temp=0
        x=-1
        y=-1
        for radek in bludiste:
            y+=1
            for seed in radek:
                x+=1
                if seed==POLICKO_SEED:
                    temp+=1
                    if temp==vybrany_seed:
                        souradnice_x=x
                        souradnice_y=y
                        break
            x=-1
        if temp==0:
            check=False
        if mapa[souradnice_y][souradnice_x]==POLICKO_SEED:
            mapa[souradnice_y][souradnice_x]=POLICKO_ZED
            smer=random.randint(0,3)
            while True:
                #0= nahoru, 1 = vpravo, 2= dolů, 3= vlevo
                if smer==0:
                    souradnice_y+=1
                if smer==1:
                    souradnice_x+=1
                if smer==2:
                    souradnice_y-=1
                if smer==3:
                    souradnice_x-=1
                
                if mapa[souradnice_y][souradnice_x]==POLICKO_ZED:
                    break
                else:
                    mapa[souradnice_y][souradnice_x]=POLICKO_ZED


def spawn_pacman(mapa):
    poloha_hrace=[1,1]
    mapa[poloha_hrace[0]][poloha_hrace[1]]=POLICKO_HRAC
    return (poloha_hrace[0],poloha_hrace[1])

def spawn_enemy(mapa):
    poloha_enemy=[MAPA_VYSKA-2,MAPA_SIRKA-2]
    mapa[poloha_enemy[0]][poloha_enemy[1]]=POLICKO_ENEMY
    return (poloha_enemy[0],poloha_enemy[1])

def odpal_zdi(mapa):
    y=-1
    x=-1
    zakazane_souradnice_x=[0,MAPA_SIRKA-1]
    zakazane_souradnice_y=[0,MAPA_VYSKA-1]
    for radek in bludiste:
        y+=1
        for policko in radek:
            x+=1
            if y not in zakazane_souradnice_y and x not in zakazane_souradnice_x:
                if policko==POLICKO_ZED:
                    roll=random.randint(0,2)
                    if roll==1:
                        mapa[y][x]=POLICKO_PRAZDNE
        x=-1           



def spocitej_vzdalenost(mapa):
    fronta=[]
    y,x=spawn_pacman(mapa)
    mapa_vzdalenosti[y][x]=0

    fronta.append(y)
    fronta.append(x)

    pouzite_souradnice=[]
    while True:
        if len(fronta)==0:
            break
        if bludiste[fronta[0]][fronta[1]+1]==POLICKO_ENEMY:
            break
        elif bludiste[fronta[0]][fronta[1]+1]==POLICKO_PRAZDNE and (fronta[0],fronta[1]+1) not in pouzite_souradnice:
            mapa_vzdalenosti[fronta[0]][fronta[1]+1]=mapa_vzdalenosti[fronta[0]][fronta[1]]+1
            fronta.append(fronta[0])
            fronta.append(fronta[1]+1)
        if bludiste[fronta[0]][fronta[1]-1]==POLICKO_ENEMY:
            break   
        elif bludiste[fronta[0]][fronta[1]-1]==0 and (fronta[0],fronta[1]-1) not in pouzite_souradnice:
            mapa_vzdalenosti[fronta[0]][fronta[1]-1]=mapa_vzdalenosti[fronta[0]][fronta[1]]+1
            fronta.append(fronta[0])
            fronta.append(fronta[1]-1)
        if bludiste[fronta[0]+1][fronta[1]]==POLICKO_ENEMY:
            break   
        elif bludiste[fronta[0]+1][fronta[1]]==POLICKO_PRAZDNE and (fronta[0]+1,fronta[1]) not in pouzite_souradnice:
            mapa_vzdalenosti[fronta[0]+1][fronta[1]]=mapa_vzdalenosti[fronta[0]][fronta[1]]+1
            fronta.append(fronta[0]+1)
            fronta.append(fronta[1])
        if bludiste[fronta[0]-1][fronta[1]]==POLICKO_ENEMY:
            break
        elif bludiste[fronta[0]-1][fronta[1]]==POLICKO_PRAZDNE and (fronta[0]-1,fronta[1]) not in pouzite_souradnice:
            mapa_vzdalenosti[fronta[0]-1][fronta[1]]=mapa_vzdalenosti[fronta[0]][fronta[1]]+1
            fronta.append(fronta[0]-1)
            fronta.append(fronta[1])
        
        pouzite_souradnice.append((fronta[0],fronta[1]))
        fronta.pop(0)
        fronta.pop(0)

        
def pohyb_enemy(mapa):
    y,x=spawn_enemy(mapa)

    okolni_cisla=[mapa_vzdalenosti[y][x+1],mapa_vzdalenosti[y][x-1],mapa_vzdalenosti[y+1][x],mapa_vzdalenosti[y-1][x]]
    temp=MAPA_VYSKA*MAPA_SIRKA
    posun=-1
    for cislo in okolni_cisla:
        posun+=1
        if cislo<temp:
            temp=cislo
            poloha_v_poli=posun
    
    smery = {
  0: "right",
  1: "left",
  2: "down",
  3: "up",}

    smer=(smery[poloha_v_poli])
    print(smer)

    slovnik = {
  "right" : (1,0),
  "left" : (-1,0),
  "down" : (0,1),
  "up" : (0,-1)}

    mapa[y][x]=POLICKO_PRAZDNE
    mapa[y+slovnik(smer)[1]][x+slovnik(smer)[0]]=POLICKO_ENEMY

bludiste = generuj_pole(0)
vytvor_okraj(bludiste)
vytvor_seedy(bludiste)
znic_seedy(bludiste)
vytvor_zdi(bludiste)
spawn_pacman(bludiste)
spawn_enemy(bludiste)
#odpal_zdi(bludiste)
vytiskni_pole(bludiste)

mapa_vzdalenosti=generuj_pole(MAPA_SIRKA*MAPA_VYSKA)
spocitej_vzdalenost(mapa_vzdalenosti)
vytiskni_pole_test(mapa_vzdalenosti)
pohyb_enemy(bludiste)

while True:
    os.system("cls")
    vytiskni_pole(bludiste)

    spocitej_vzdalenost(mapa_vzdalenosti)
    pohyb_enemy(bludiste)
    time.sleep(1)
    