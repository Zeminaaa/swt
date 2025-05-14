with open("data.txt","r") as soubor:
    data=soubor.read()

#print(data)

list_of_nums=["0","1","2","3","4","5","6","7","8","9"]
p=[]
temp=""

for znak in data:
    if znak in list_of_nums:
        temp+=znak
    else:
        if temp!="":
            p.append(temp)
        temp=""
p.append(temp)

maticeA=[]
maticeB=[]
counter=0

for znak in p:
    if counter<25:
        maticeA.append(znak)
    else:
        maticeB.append(znak)
    counter+=1

def vypis(matice):
    counter=0
    velikost=len(matice)**0.5
    for znak in matice:
        print(znak,end=" ")
        counter+=1
        if counter==velikost:
            print("")
            counter=0
    print("")

    

vypis(maticeA)
vypis(maticeB)