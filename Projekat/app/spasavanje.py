from datetime import datetime


class Spasavanje:
    def __init__(self):
        self.id = -1
        self.ime_i_prezime=""
        self.datum_i_vreme = (datetime.now()).strftime("%d.%m.%Y %H:%M")
        self.oznaka_spasioca = ""
        self.trajanje_spasavanja = -1
        self.status=1
    def vrati_vrednost(self):
        return {"id": self.id, "ime_i_prezime":self.ime_i_prezime, "datum_i_vreme":self.datum_i_vreme,
                "oznaka_spasioca":self.oznaka_spasioca,"trajanje_spasavanja":self.trajanje_spasavanja,
                "status":self.status}
    def postavi_vrednost(self, objekat):
        self.id = int(objekat["id"])
        self.ime_i_prezime = objekat["ime_i_prezime"]
        self.datum_i_vreme = objekat["datum_i_vreme"]
        self.oznaka_spasioca = objekat["oznaka_spasioca"]
        self.trajanje_spasavanja = int(objekat["trajanje_spasavanja"])
        self.status = objekat["status"]
    def pravljenje_objekta(self):
        self.id = int(input("Unesite evidencioni broj:"))
        while True:
            if(self.id > 10**7):
                print("Evidencioni broj mora biti 7 cifara.")
                self.id = int(input("Unesite evidencioni broj:"))
            else:
                break
        self.ime_i_prezime = input("Ime i prezime spasenog:")
        #self.datum_i_vreme = (datetime.now()).strftime("%d.%m.%Y %H:%M")
        self.datum_i_vreme = input("Datum i vreme:")
        self.oznaka_spasioca = input("Oznaka spasioca:")
        while True:
            if len(self.oznaka_spasioca)!=5:
                self.oznaka_spasioca = input("Oznaka spasioca mora biti tacno 5 karaktera:")
            else:
                break
        self.trajanje_spasavanja = int(input("Trajanje spasavanja:"))
        while True:
            if self.trajanje_spasavanja>4320:
                self.trajanje_spasavanja = int(input("Mora biti manje ili jednako 4320 minuta:"))
            else:
                break
        self.status=1
    def logicko_brisanje(self):
        self.status = 0
    def promena_vrednosti(self):
        while True:
            print("Izaberite koji cete atribut da promenite( 0 je za kraj):\n"
                  "1.Evidencioni broj\n"
                  "2.Ime i prezime spasenog\n"
                  "3.Datum i vreme\n"
                  "4.Oznaka spasioca\n"
                  "5.Trajanje spasavanja")
            unos = int(input("Unesite opciju:"))
            if unos==0:
                break
            if unos==1:
                self.id = int(input("Unesite evidencioni broj:"))
                while True:
                    if (self.id > 10 ** 7):
                        print("Evidencioni broj mora biti 7 cifara.")
                        self.id = int(input("Unesite evidencioni broj:"))
                    else:
                        break
            if unos==2:
                self.ime_i_prezime = input("Ime i prezime spasenog:")
            if unos == 3:
                self.datum_i_vreme = input("Datum i vreme:")
            if unos==4:
                self.oznaka_spasioca = input("Oznaka spasioca:")
                while True:
                    if len(self.oznaka_spasioca) != 5:
                        self.oznaka_spasioca = input("Oznaka spasioca mora biti tacno 5 karaktera:")
                    else:
                        break
            if unos==5:
                self.trajanje_spasavanja = int(input("Trajanje spasavanja:"))
                while True:
                    if self.trajanje_spasavanja > 4320:
                        self.trajanje_spasavanja = int(input("Mora biti manje ili jednako 4320 minuta:"))
                    else:
                        break
