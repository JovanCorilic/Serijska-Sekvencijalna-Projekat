
from app.record import *
from app.binary_file import *
from app.constants import *
from app.sequential_file import *
from app.serial_file import *
from os.path import exists
from app.spasavanje import Spasavanje


if __name__ == '__main__':
    binary_file = ""
    binary_file_izlazna=""
    binary_file_greska=""
    while True:
        print("Sta zelite od opcija (unesite broj da odaberete, 0 za iskljucivanje programa):\n"
              "1.Formiranje prazne datoteke\n"
              "2.Izbor aktivne datoteke zadavanjem njenog naziva\n"
              "3.Prikaz naziva aktivne datoteke\n"
              "4.Pocni operaciju\n"
              "5.Ispis aktivne, izlazne i datoteke gresaka\n"
              "6.Ucitati test primer")
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
            attributesTemp = ["id", "ime_i_prezime", "datum_i_vreme", "oznaka_spasioca", "trajanje_spasavanja",
                              "status"]
            fmtTemp = "i60s17s5sii"
            rec = Record(attributesTemp, fmtTemp, CODING)
            binary_file=SequentialFile(naziv,rec,F)

            putanja = binary_file.filename.split(".")[0] + "serial.dat"
            rec = Record(ATTRIBUTES, FMT, CODING)
            binary_file_serial = SerialFile(putanja, rec, F)
            binary_file_serial.init_file()
        if(unos==3):
            if binary_file!="":
                print("Naziv fajla: " + binary_file.filename.split("/")[1])
            else:
                print("Niste odabrali aktivni fajl!")
        if(unos==4):
            if binary_file == "":
                print("Morate uneti naziv aktivne datoteke!")
                continue
            putanja = binary_file.filename.split(".")[0] + "serial.dat"
            rec = Record(ATTRIBUTES, FMT, CODING)
            binary_file_serial = SerialFile(putanja, rec, F)
            binary_file_serial.init_file()
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
                        temp = Spasavanje()
                        temp.pravljenje_objekta()
                        binary_file_serial.insert_record_no_id_check(temp.vrati_vrednost())
                if unos==2:
                    if(binary_file!=""):
                        temp = Spasavanje()
                        temp.promena_vrednosti()
                        binary_file_serial.insert_record_no_id_check(temp.vrati_vrednost())
                if unos == 3:
                    if(binary_file!=""):
                        temp = Spasavanje()
                        temp.logicko_brisanje()
                        binary_file_serial.insert_record_no_id_check(temp.vrati_vrednost())
                if unos == 4:
                    if (binary_file != ""):
                        temp = Spasavanje()
                        temp.pravo_brisanje()
                        binary_file_serial.insert_record_no_id_check(temp.vrati_vrednost())

            lista = binary_file_serial.get_sorted_content_of_file()

            putanjaDruga = binary_file.filename.split(".")[0] + "sequential.dat"
            rec = Record(ATTRIBUTES, FMT, CODING)
            binary_file_sequential = SequentialFile(putanjaDruga, rec, F)
            binary_file_sequential.init_file()

            for i in lista:
                binary_file_sequential.insert_record_no_id_check(i)

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
            binary_file_izlazna = SequentialFile(putanja, rec, F)
            binary_file_izlazna.init_file_aktivna_datoteka()
            binary_file_izlazna.kopiranje(binary_file)

            binary_file_sequential.mergovanje_izlazne_aktivne(binary_file_izlazna, binary_file_greska)

        if unos == 5:
            if binary_file!="" and binary_file_izlazna!="" and binary_file_greska!="":
                print("Aktivna datoteka")
                binary_file.print_file()
                print("Izlazna datoteka")
                binary_file_izlazna.print_file()
                print("Datoteka gresaka")
                binary_file_greska.print_file()

        if unos==6:
            if binary_file!="":
                with open("data/test.csv", "r") as f:
                    while True:
                        temp = f.readline()
                        if not temp:
                            break
                        lista = temp.split(",")

                        binary_file.insert_record({"id":int(lista[0]),"ime_i_prezime":lista[1],"datum_i_vreme":lista[2],"oznaka_spasioca":lista[3],"trajanje_spasavanja":int(lista[4]),"status":1})







