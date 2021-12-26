
from app.record import *
from app.binary_file import *
from app.constants import *
from app.sequential_file import *
from app.serial_file import *
from os.path import exists
from app.spasavanje import Spasavanje


if __name__ == '__main__':
    binary_file =  ""
    while True:
        print("Sta zelite od opcija (unesite broj da odaberete, 0 za iskljucivanje programa):\n"
              "1.formiranje prazne datoteke pri čemu korisnik zadaje naziv nove datoteke\n"
              "2.izbor aktivne datoteke zadavanjem njenog naziva\n"
              "3.prikaz naziva aktivne datoteke\n"
              "4.vodeće serijske datoteke promena")
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
        if(unos==4):
            binary_file_serial=""
            while True:
                print("1.Napraviti slog\n"
                      "2.Izmeniti slog\n"
                      "3.Logicki izbrisati slog\n"
                      "4.Fizicki izbrisati slog\n"
                      "0.Natrag")
                unos = int(input("Unesite opciju ovde:"))
                if unos==0:
                    break
                if unos==1:
                    if(binary_file!=""):
                        putanja = binary_file.filename.split(".")[0] + "serial.dat"
                        rec = Record(ATTRIBUTES, FMT, CODING)
                        binary_file_serial = SerialFile(putanja, rec, F)
                        if not (exists(putanja)):
                            binary_file_serial.init_file()
                        temp = Spasavanje()
                        temp.pravljenje_objekta()
                        binary_file_serial.insert_record(temp.vrati_vrednost())
                if unos==2:
                    if(binary_file!=""):
                        putanja = binary_file.filename.split(".")[0] + "serial.dat"
                        rec = Record(ATTRIBUTES, FMT, CODING)
                        binary_file_serial = SerialFile(putanja, rec, F)
                        binary_file_serial.change_by_id(int(input("Unesite evidencioni broj:")))
                if unos == 3:
                    if(binary_file!=""):
                        putanja = binary_file.filename.split(".")[0] + "serial.dat"
                        rec = Record(ATTRIBUTES, FMT, CODING)
                        binary_file_serial = SerialFile(putanja, rec, F)
                        binary_file_serial.logical_delete_by_id(int(input("Unesite evidencioni broj:")))
                if unos == 4:
                    if (binary_file != ""):
                        putanja = binary_file.filename.split(".")[0] + "serial.dat"
                        rec = Record(ATTRIBUTES, FMT, CODING)
                        binary_file_serial = SerialFile(putanja, rec, F)
                        binary_file_serial.delete_by_id(int(input("Unesite evidencioni broj:")))




