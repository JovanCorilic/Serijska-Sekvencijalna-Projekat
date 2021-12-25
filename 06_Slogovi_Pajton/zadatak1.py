import struct

IN_FILE = "tacke.csv"
OUT_FILE="tacke.bin"
FORMAT = "ff"
DELIMITER = " "
ENCODING = "ascii"

DIMENZIONALNOST = 2
with open(IN_FILE) as provera:
    lines = provera.readlines()

    BROJTACAKA = len(lines)*2


with open(IN_FILE) as unos, open(OUT_FILE, "wb") as ispis:
    record = (BROJTACAKA,DIMENZIONALNOST)
    record = [v.encode(ENCODING) if isinstance(v, str) else v for v in record]
    write_bytes = struct.pack(FORMAT, *record)
    ispis.write(write_bytes)

    while True:
        line = unos.readline()
        if not line:
            break
        fields = line.split(DELIMITER)
        record = (float(fields[0]), float(fields[1]))
        record = [v.encode(ENCODING) if isinstance(v , str) else v for v in record]
        write_bytes = struct.pack(FORMAT,*record)
        ispis.write(write_bytes)

if __name__ == '__main__':
    pass