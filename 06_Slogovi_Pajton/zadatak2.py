
import struct

IN_FILE = "tacke.bin"
FORMAT = "ff"
ENCODING = "ascii"
RECORDSIZE = struct.calcsize(FORMAT)

with open(IN_FILE, "rb") as unos:
    unos.seek(RECORDSIZE)
    br = 1
    while True:
        unos.seek(br*RECORDSIZE)
        record_bytes = unos.read(RECORDSIZE)

        if record_bytes == b'':
            break
        record = struct.unpack(FORMAT, record_bytes)
        record = [v.decode(ENCODING).strip('\x00') if isinstance(v,bytes) else v for v in record ]
        print(record)
        br+=1
if __name__ == '__main__':
    pass