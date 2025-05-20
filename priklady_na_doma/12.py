slovnik={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
vysledek={}

for vec in slovnik:
    temp=[]
    for cislo in slovnik[vec]:
        if cislo%2==0:
            temp.append(cislo)
    slovnik[vec]=temp

print(slovnik)