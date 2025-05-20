slovniky = [{'Obilí': 90, 'Zelenina': 92}, {'Obilí': 89, 'Zelenina': 94}, {'Obilí': 92, 'Zelenina': 88}]
vystup=[]
for slovnik in slovniky:
    for char in slovnik:
        if char=="Zelenina":
            vystup.append(slovnik[char])

print(vystup)