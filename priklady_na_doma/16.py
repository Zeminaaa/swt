#vstup = input("zadejte heslo:")
vstup="ABd1234@1,a F1#,2w3E*,2We3345,ahoj"
hesla=[]

temp=""
for char in vstup:
    if char != ",":
        temp+=char
    elif char == ",":
        hesla.append(temp)
        temp=""
hesla.append(temp)

for heslo in hesla:
    for char in heslo:
        pass