import csv

seznam_vsech_knih=[]

def zapsat_list_do_csv(list_radku, nazev_souboru):
    """Zapíše list řádků do souboru CSV."""

    with open(nazev_souboru, 'w', newline='', encoding='utf-8') as soubor_csv:
#   možné zapsat i takto:
#   soubor_csv = open(nazev_souboru, 'w', newline='', encoding='utf-8')
        zapisovac = csv.writer(soubor_csv)
        zapisovac.writerows(list_radku)

def nacist_csv_do_listu(nazev_souboru):
    """Načte data z CSV souboru do listu řádků."""

    list_radku = []
    with open(nazev_souboru, 'r', encoding='utf-8') as soubor_csv:
        ctec = csv.reader(soubor_csv)
        for radek in ctec:
            list_radku.append(radek)
    return list_radku

class Kniha():
    def __init__(self,nazev, autor,rok_vydani,id = None):
        self.nazev = nazev
        self.autor = autor
        self.rok_vydani = rok_vydani
        self.id = id
        self.pujcena = False
        self.format = None

    def pujc_knihu(self):
        if self.pujcena == False: # je kniha k dispozici?
            self.pujcena = True
            return True # uspesne provedeno
        else:
            return False # kniha jiz byla pujcena, neuspech

    def vrat_knihu(self):
        if self.pujcena == True: # byla kniha vypujcena ?
            self.pujcena = False
            return True # kniha je zpet, uspesne provedeno
        else:
            return False # kniha nebyla pryc, nemam co vratit

    def set_id(self, id): # setter pro ID - nastavi hodnotu id v objektu
        self.id = id

    def get_id(self): # getter pro ID - vrati hodnotu id v objektu
        return self.id

    def popis(self):    # vytikne popis objektu
        print(f"kniha : {self.nazev} ({self.autor}) - {self.rok_vydani}", end="")
        if self.format==None:
            print(", papírová kniha")

    def rozdel_udaje(self,pole):
        pole.append(self.nazev)
        pole.append(self.autor)
        pole.append(self.id)
        pole.append(self.rok_vydani)
        
    def set_autor(self, autor): #setter pro autora - nastavi hodnotu promenne autor v objektu
        self.autor = autor
    
    def get_autor(self):    # getter pro autora - vrati hodnotu promenne autor v objektu
        return self.autor

    


class EKniha(Kniha):
    def __init__(self, nazev, autor, rok_vydani,format,id = None):
        super().__init__(nazev, autor, rok_vydani, id = id)
        self.format = format

    def popis(self):
        print(f"ekniha : {self.nazev} ({self.autor}) - {self.rok_vydani}, {self.format}")


class Knihovna:
    def __init__(self):
        self.knihy = []
        self.last_id = 0

    def pridej_knihu(self, kniha):
        self.last_id+=1
        kniha.set_id(self.last_id)
        self.knihy.append(kniha)


    def odeber_knihu(self, id):
        for i,kniha in enumerate(self.knihy):
            if kniha.get_id() == id:
                self.knihy.pop(i)
                return
            
    def najdi_knihu(self,id):
        for kniha in self.knihy:
            if kniha.get_id() == id:
                return kniha
        return None

    def pujc_knihu(self, id):
        kniha = self.najdi_knihu(id)
        if kniha != None:
            return kniha.pujc_knihu()
        else:
            return False
        
    def vrat_knihu(self, id):
        kniha = self.najdi_knihu(id)
        return False if kniha == None else kniha.vrat_knihu()

    def seznam_knih(self):
        for kniha in self.knihy:
        
            print(f"ID: {kniha.get_id()}", end=" / ")
            kniha.popis()

    def uloz_knihy(self):
        for kniha in self.knihy:
            temp=[]
            kniha.rozdel_udaje(temp)
            seznam_vsech_knih.append(temp)
        

mojekniha = Kniha("špalíček pohádek","František Vodvářka", 1808)
mojekniha3 = Kniha("potkali se u kolina 3","Mroz Pumlicovlastnic", 1997)
mojekniha2 = EKniha("cesta z mesta","lubo", 1389,"epub")


zk = Knihovna()

zk.pridej_knihu(Kniha("špalíček pohádek","František Vodvářka", 1808))
zk.pridej_knihu(mojekniha2)
#zk.seznam_knih()

zk.uloz_knihy()
#print(seznam_vsech_knih)

zapsat_list_do_csv(seznam_vsech_knih, "data_z_knihovny.csv")

#seznam_vsech_knih=nacist_csv_do_listu("data_z_knihovny.csv")