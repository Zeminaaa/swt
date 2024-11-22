# Vykresli šachovnici dle zadání :  
sirka=int(input("zadej šířku: "))
vyska=int(input("zadej výšku: "))

for i in range(vyska):
    for i in range(sirka):
        print("o  ",end="")
        print("x  ",end="")
    print("")
    for i in range(sirka):
        print("x  ",end="")
        print("o  ",end="")
    print("")