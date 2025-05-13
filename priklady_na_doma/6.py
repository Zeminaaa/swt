# slovnik={}
# pocet_klicu=int(input("Zadej kolik chceš mít ve slovníku klíčů: "))
# posun=1
# for klic in range(pocet_klicu):
#     pismena=input("zadej písmena do klíče: ")
#     temp=[]
#     for pismeno in pismena:
#         temp.append(pismeno)
#     slovnik[posun]=(temp)
#     posun+=1
# print(slovnik)

slovnik={1: ['a', 'b'], 2: ['c', 'd']}

for p1 in slovnik[1]:
    for p2 in slovnik[2]:
        print(p1 + p2)

