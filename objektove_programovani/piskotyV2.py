velikost=int(input("Zadej velikost hrací plochy: "))
vyherni_rada=int(input("Zadej jak dlouhá má být výherní řada: "))

class Sachovnice:
    def __init__(self,velikost=velikost):
        self.velikost=velikost
        self.policka=[["." for sloupec in range(velikost)] for radek in range(velikost)]
    
    def tah(self, radek, sloupec, hodnota):
        radek -= 1
        sloupec -= 1
        if self.policka[radek][sloupec]==".":
            self.policka[radek][sloupec] = hodnota
        else:
            print("Toto pole je už obsazené!")
    
    def vytiskni(self):
        for radek in self.policka:
            for pole in radek:
                print(pole,end=" ")
            print("")

    def zkontroluj_vyhru(self, radek, sloupec, hodnota):
        radek -= 1
        sloupec -= 1

        def kontroluj_smer(zmena_radek, zmena_sloupec):
            rada = 1
            posun = 1

            # dopredu
            while True:
                novy_radek = radek + zmena_radek * posun
                novy_sloupec = sloupec + zmena_sloupec * posun
                if 0 <= novy_radek < self.velikost and 0 <= novy_sloupec < self.velikost:
                    if self.policka[novy_radek][novy_sloupec] == hodnota:
                        rada += 1
                        posun += 1
                    else:
                        break
                else:
                    break

            posun = 1
            # zpatky po tom co to uz dalsi nenajde
            while True:
                novy_radek = radek - zmena_radek * posun
                novy_sloupec = sloupec - zmena_sloupec * posun
                if 0 <= novy_radek < self.velikost and 0 <= novy_sloupec < self.velikost:
                    if self.policka[novy_radek][novy_sloupec] == hodnota:
                        rada += 1
                        posun += 1
                    else:
                        break
                else:
                    break

            return rada >= vyherni_rada

        # Zkontroluj všechny směry
        if kontroluj_smer(0, 1):  # vodorovne
            return True
        if kontroluj_smer(1, 0):  # svisle
            return True
        if kontroluj_smer(1, 1):  # diagonála doprava dolu
            return True
        if kontroluj_smer(1, -1): # diagonála doleva dolu
            return True

        return False

        


def zacni_hru():
    hra=Sachovnice()
    hrac="O"

    while True:
        hra.vytiskni()
        radek=int(input(f"Zadej číslo řádku na které chceš umístit {hrac}: "))
        sloupec=int(input(f"Zadej číslo sloupce na které chceš umístit {hrac}: "))
        hra.tah(radek, sloupec, hrac)

        if hra.zkontroluj_vyhru(radek,sloupec,hrac)==True:  #kontrola výhry
            hra.vytiskni()
            print(f"Hra skončila výhrou hráče: {hrac}")
            break

        if hrac=="O":   #změna hráče
            hrac="X"
        else:
            hrac="O"

        
zacni_hru()
