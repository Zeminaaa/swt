velikost=int(input("zadej kolik vepsaných čtverců chceš: "))
plny=(4*velikost)+1
mezery=(3*velikost)+(velikost-1)-2
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





for i in range(posun):
        
        print("*  ",end="")
        print("   ",end="")
print("*  ",end="")
for i in range(posun):
        print("   ",end="")
        print("*  ",end="")
print("")


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