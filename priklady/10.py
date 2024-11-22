# Napište program, který  mezi každá dvě písmena daného textu vloží dodaný text. 
text=input("zadej text: ")
vklad=input("zadej co chceš vepsat: ")
p=[]
delka=len (text)
for pismeno in text:
    p.append(pismeno)

for pismeno in p:
    print(pismeno,end="")
    if delka>1:
        print(vklad,end="")
    delka-=1