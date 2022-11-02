from app.record import *
from  app.binary_file import *
from app.constants import *
from app.serial_file import *

if __name__ == '__main__':

    unos = True
    rows = []
    while unos:
        print("Zelite li da unesete zatvorenike?")
        broj = int(input("Ovde unesite"))
        if broj == 0:
            unos = False
            break
        rows.append({
            "id":int(input("Evidencioni broj:")),
            "sifra_zatvorenika":str(input("Sifra zatvorenika:")),
            "datum_vreme":str(input("Datum i vreme:")),
            "oznaka_celije":str(input("Oznaka celije:")),
            "duzina_kazne":int(input("duzina_kazne:"))
        })
    if rows:
        naziv = "data/"+str(input("Unesite naziv datoteke"))+".dat"
        rec = Record(ATTRIBUTES,FMT,CODING)
        binary_file = SerialFile(naziv,rec,F)
        binary_file.init_file()

        for i in rows:
            binary_file.insert_record(i)

        binary_file.print_file()
        print(binary_file.find_by_id(1))
        binary_file.change_by_id(1)
        binary_file.print_file()




