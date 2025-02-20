class Kniha:
    def __init__(self,nazev,autor,rok_vydani):
        self.nazev = nazev
        self.autor = autor
        self.rok_vydani=rok_vydani
    def popis(self):
        return f"{self.nazev}, {self.autor} : {self.rok_vydani}"
    
    def set_autor(self,autor):
        self.autor=autor

    def get_autor(self):
        return self.autor
    
class Ekniha(Kniha):
    def __init__(self,nazev,autor,rok_vydani,format):
        super().__init__(nazev,autor,rok_vydani)
        self.format=format

    def popis(self):
        return super().popis() + f", format : {self.format}"

moje_kniha=Kniha("Z kazdeho rozku trosku","Leman","1984")

knihovna=[
    Kniha("bobes","lemenemn","845"),
    Kniha("probehy o kocouru","zemelmeman","1985"),
    Ekniha("ekniha o tivote","zabakoruv pisar","2012","ebook")
]

moje_kniha.set_autor("Pikovej kral")

print(moje_kniha.autor)
print(moje_kniha.nazev)
print(moje_kniha.rok_vydani)

print(moje_kniha.popis())

for kniha in knihovna:
    print(kniha.popis())