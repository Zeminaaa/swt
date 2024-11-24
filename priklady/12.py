# Napište program, který  zcenzuruje dodaný řetězec tak, že každý druhý znak nahradí za X. 
p=[]
text=input("zadej co chceš: ")
for znak in text:
    p.append(znak)
p[1::2]=["x"]*len(p[1::2])
for znak in p:
    print(znak,end="")
