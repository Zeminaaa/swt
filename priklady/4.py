# Vykresli diamant dle zadání : 
sirka=int(input("zadej šířku: "))
mezery=int((sirka-1)/2)
plny=int(sirka-(2*mezery))
switch=False

for i in range(sirka):
    for i in range(mezery):
        print("   ",end="")
    for i in range(plny):
        print("#  ",end="")
    for i in range(mezery):
        print("   ",end="")
    if mezery==0:
        switch=True
    if switch==False:
        plny+=2
        mezery-=1
    if switch:
        plny-=2
        mezery+=1
    print("")
    