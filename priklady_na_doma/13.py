vstup=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI '], [5, 'Zachary Simon', 'VII']]
vystup={}

for polozka in vstup:
    vystup[polozka[0]] = polozka[1:]

print(vystup)