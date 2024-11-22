# Napište program, který vypíše prvních n prvků posloupnosti, jejíž první prvky vypadají následovně: 
pocet=int(input("zadej číslo: "))
pole=[]
nasobitel=1

for temp in range(pocet):
    temp=nasobitel
    pole.append(temp)
    pole.append(-temp)
    nasobitel+=1

for char in pole:
    print(char,end=" ")