#4. Výpočet součtu čísel v seznamu 
#Napište funkci, která vezme seznam čísel jako vstup a vrátí jejich součet. Otestujte ji na seznamu [1, 2, 3, 4, 5]. 

numbers=[1, 2, 3, 4, 5]
#print(sum(numbers))              hádám že takhle to asi udělat nesmim
total=0
for num in numbers:
    total+=num
print(total)