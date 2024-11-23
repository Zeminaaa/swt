# V textové grafice vykresli n vnořených čtverců dle zadání (pro 
velikost=int(input("zadej kolik vepsaných čtverců chceš: "))
plny=(4*velikost)+1
mezery=(3*velikost)+(velikost-3)
posun=0

for i in range(velikost):

    for i in range(posun):
        
        print("*  ",end="")
        print("   ",end="")
    
    for i in range(plny):
        print("*  ",end="")
    plny-=4    
    for i in range(posun):
        print("   ",end="")
        print("*  ",end="")
    posun+=1
    print("")

    for i in range(posun):
        print("*  ",end="")
        print("   ",end="")
    for i in range(mezery):
        print("   ",end="")
    mezery-=4
    for i in range(posun):
        print("   ",end="")
        print("*  ",end="")
    print("")

# tohle printnulo svrchní polovinu bez středového řádku
# tam kde se používá range posun, tak se střídavě printuje * a mezera.
# tam kde se používá range plny a mezery, tak se printuje buď určitý počet mezer, nebo *, to se vždy děje uprostřed



for i in range(posun):
        
        print("*  ",end="")
        print("   ",end="")
print("*  ",end="")
for i in range(posun):
        print("   ",end="")
        print("*  ",end="")
print("")

# tohle printnulo středový řádek, zase nejdřív střídavě * a mezera, následně 1x*, poté zase střídavě mezera a *

plny+=4
mezery+=4
posun-=0



for i in range(velikost):


    for i in range(posun):
        print("*  ",end="")
        print("   ",end="")
    for i in range(mezery):
        print("   ",end="")
    mezery+=4
    for i in range(posun):
        print("   ",end="")
        print("*  ",end="")
    print("")
    posun-=1

    for i in range(posun):
        print("*  ",end="")
        print("   ",end="")
    for i in range(plny):
        print("*  ",end="")
    plny+=4
    for i in range(posun):
        print("   ",end="")
        print("*  ",end="")
    print("")
    # tohle stejným principem printnulo spodní polovinu bez středového řádku
