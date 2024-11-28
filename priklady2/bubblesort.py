p=[]
while True:
    num=input("zadej číslo: ")
    if num=="":
        break
    num=int(num)
    p.append(num)



for i in range(len(p)):
    posun=0
    for i in range(len(p)-1):
        
        if p[posun]>p[posun+1]:
            temp=p[posun+1]
            p[posun+1]=p[posun]
            p[posun]=temp
        posun+=1


print(p)