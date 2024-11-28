p=[]
while True:
    num=input("zadej číslo: ")
    if num=="":
        break
    num=int(num)
    p.append(num)

check_if_swapped=True

while check_if_swapped:
    posun=0
    check_if_swapped=False
    for i in range(len(p)-1):
        
        if p[posun]>p[posun+1]:
            temp=p[posun+1]
            p[posun+1]=p[posun]
            p[posun]=temp
            check_if_swapped=True
        posun+=1


print(p)
