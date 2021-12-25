
from app.record import *
from app.binary_file import *
from app.constants import *
from app.sequential_file import *
from app.serial_file import *


if __name__ == '__main__':
    binary_file =  ""
    while True:
        print("Sta zelite od opcija (unesite broj da odaberete, 0 za iskljucivanje programa):\n"
              "1.formiranje prazne datoteke pri čemu korisnik zadaje naziv nove datoteke\n"
              "2.izbor aktivne datoteke zadavanjem njenog naziva\n"
              "3.prikaz naziva aktivne datoteke")
        unos = int(input("Unesite ovde opciju:"))
        if(unos==0):
            break
        if(unos==1):
            naziv = "data/"+str(input("Unesite naziv datoteke:"))+".dat"
            rec = Record(ATTRIBUTES,FMT,CODING)
            binary_file = SequentialFile(naziv,rec,F)
            binary_file.init_file()
        if(unos==2):
            naziv="data/"+str(input("Unesite naziv aktivne datoteke:"))+".dat"
            rec = Record(ATTRIBUTES,FMT,CODING)
            binary_file=SequentialFile(naziv,rec,F)
        if(unos==3):
            if binary_file!="":
                print("Naziv fajla " + binary_file.filename)
            else:
                print("Niste odabrali aktivni fajl!")
