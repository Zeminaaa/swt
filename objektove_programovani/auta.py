class Auto:
    def __init__(self,znacka,model,rok_vydani,barva):
        self.znacka = znacka
        self.model = model
        self.rok_vydani=rok_vydani
        self.barva=barva

    def popis(self):
        return f"značka: {self.znacka}, model: {self.model}, rok výroby: {self.rok_vydani}, barva: {self.barva}"


class NakladniAuto(Auto):
    def __init__(self,znacka,model,rok_vydani,barva,nosnost):
        super().__init__(znacka,model,rok_vydani,barva)
        self.nosnost=nosnost
    
    def popis(self):
        return super().popis() + f", nosnost : {self.nosnost}"

moje_auto=Auto("skoda","fabia","2012","cerna")
muj_nakladak=NakladniAuto("tatra","nejlepsi","1964","zelena","6000kg")


auta=[
    moje_auto,
    muj_nakladak
]

#print(moje_auto.popis())
#print(muj_nakladak.popis())

for auto in auta:
    print(auto.popis())
