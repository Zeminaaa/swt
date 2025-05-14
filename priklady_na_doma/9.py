with open("data.txt","r") as soubor:
    data=soubor.readline()

list_of_nums=["0","1","2","3","4","5","6","7","8","9"]
serazene=[]
temp=""

for znak in data:
    if znak in list_of_nums:
        temp+=znak
    else:
        if temp!="":
            serazene.append(temp)
        temp=""

#print(data)

check_if_swapped=True

while check_if_swapped:
    posun=0
    check_if_swapped=False
    for i in range(len(serazene)-1):
        
        if int(serazene[posun])>int(serazene[posun+1]):
            temp=serazene[posun+1]
            serazene[posun+1]=serazene[posun]
            serazene[posun]=temp
            check_if_swapped=True
        posun+=1

#print(serazene)

with open("vysledek.txt","w") as soubor:
    soubor.write(data)
    for cislo in serazene:
        soubor.write(cislo+" ")