
from app.record import *
from app.binary_file import *
from app.constants import *
from app.sequential_file import *
from app.serial_file import *
from os.path import exists
from app.spasavanje import Spasavanje


if __name__ == '__main__':
    binary_file = ""
    while True:
        print("Sta zelite od opcija (unesite broj da odaberete, 0 za iskljucivanje programa):\n"
              "1.formiranje prazne datoteke pri čemu korisnik zadaje naziv nove datoteke\n"
              "2.izbor aktivne datoteke zadavanjem njenog naziva\n"
              "3.prikaz naziva aktivne datoteke\n"
              "4.vodeće serijske datoteke promena\n"
              "5.sekvencijalne datoteke promena\n"
              "6.izlazne sekvencijalne datoteke")
        unos = int(input("Unesite ovde opciju:"))
        if(unos==0):
            break
        if(unos==1):
            naziv = "data/"+str(input("Unesite naziv datoteke:"))+".dat"
            attributesTemp = ["id", "ime_i_prezime", "datum_i_vreme","oznaka_spasioca", "trajanje_spasavanja", "status"]
            fmtTemp = "i60s17s5sii"
            rec = Record(attributesTemp,fmtTemp,CODING)
            binary_file = SequentialFile(naziv,rec,F)
            binary_file.init_file_aktivna_datoteka()

            putanja = binary_file.filename.split(".")[0] + "serial.dat"
            rec = Record(ATTRIBUTES, FMT, CODING)
            binary_file_serial = SerialFile(putanja, rec, F)
            binary_file_serial.init_file()


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
                        binary_file_serial.insert_record_no_id_check(temp.vrati_vrednost())
                if unos==2:
                    if(binary_file!=""):
                        putanja = binary_file.filename.split(".")[0] + "serial.dat"
                        rec = Record(ATTRIBUTES, FMT, CODING)
                        binary_file_serial = SerialFile(putanja, rec, F)
                        if not (exists(putanja)):
                            binary_file_serial.init_file()
                        temp = Spasavanje()
                        temp.promena_vrednosti()
                        binary_file_serial.insert_record_no_id_check(temp.vrati_vrednost())
                if unos == 3:
                    if(binary_file!=""):
                        putanja = binary_file.filename.split(".")[0] + "serial.dat"
                        rec = Record(ATTRIBUTES, FMT, CODING)
                        binary_file_serial = SerialFile(putanja, rec, F)
                        temp = Spasavanje()
                        temp.logicko_brisanje()
                        binary_file_serial.insert_record_no_id_check(temp.vrati_vrednost())
                if unos == 4:
                    if (binary_file != ""):
                        putanja = binary_file.filename.split(".")[0] + "serial.dat"
                        rec = Record(ATTRIBUTES, FMT, CODING)
                        binary_file_serial = SerialFile(putanja, rec, F)
                        temp = Spasavanje()
                        temp.pravo_brisanje()
                        binary_file_serial.insert_record_no_id_check(temp.vrati_vrednost())
        if unos==5:
            if binary_file!="":
                putanja = binary_file.filename.split(".")[0] + "serial.dat"
                rec = Record(ATTRIBUTES, FMT, CODING)
                binary_file_serial = SerialFile(putanja, rec, F)
                lista = binary_file_serial.get_sorted_content_of_file()
                putanjaDruga = binary_file.filename.split(".")[0] + "sequential.dat"
                rec = Record(ATTRIBUTES, FMT, CODING)
                binary_file_sequential = SequentialFile(putanjaDruga, rec, F)

                binary_file_sequential.init_file()
                for i in lista:
                    binary_file_sequential.insert_record_no_id_check(i)
                binary_file_serial.init_file()
        if unos==6:
            if binary_file!="":
                putanja = binary_file.filename.split(".")[0] + "sequential.dat"
                rec = Record(ATTRIBUTES, FMT, CODING)
                binary_file_sequential = SequentialFile(putanja, rec, F)

                putanjaGreska = binary_file.filename.split(".")[0] + "greske.dat"
                tempAttributes = ["id", "opis_greske"]
                tempFMT = "i100s"
                rec = Record(tempAttributes, tempFMT, CODING)
                binary_file_greska = SequentialFile(putanjaGreska, rec, F)
                binary_file_greska.init_file_datoteka_gresaka()

                putanja = binary_file.filename.split(".")[0] + "izlazna.dat"
                attributesTemp = ["id", "ime_i_prezime", "datum_i_vreme", "oznaka_spasioca", "trajanje_spasavanja",
                                  "status"]
                fmtTemp = "i60s17s5sii"
                rec = Record(attributesTemp, fmtTemp, CODING)
                binary_file_izlazna = SequentialFile(putanja,rec,F)
                binary_file_izlazna.init_file_aktivna_datoteka()
                binary_file_izlazna.kopiranje(binary_file)

                lista = binary_file_sequential.mergovanje_izlazne_aktivne(binary_file_izlazna,binary_file_greska)
                binary_file_izlazna.print_file()
        if unos == 7:
            if binary_file!="":
                binary_file.print_file()








