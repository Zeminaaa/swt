# Napište program, který  zcenzuruje dodaný řetězec tak, že každý druhý znak nahradí za X. 
p=[]
while True:
    temp=input("zadej co chceš, pokud jen odentruješ zrušíš zadávání: ")
    if temp=="":
        break
    p.append(temp)

p[1::2]=["x"]*len(p[1::2])
print(p)