vstup=("Hello world!")
v_pismena=0
m_pismena=0
for char in vstup:
    if char.isupper():
        v_pismena+=1
    if char.islower():
        m_pismena+=1

print(f"VELKÁ PÍSMENA {v_pismena}\nMALÁ PÍSMENA {m_pismena}")