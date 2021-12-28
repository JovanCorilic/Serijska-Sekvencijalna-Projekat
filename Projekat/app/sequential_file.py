#!/usr/bin/python

import os

from app.binary_file import BinaryFile


class SequentialFile(BinaryFile):
    def __init__(self, filename, record, blocking_factor, empty_key=-1):
        BinaryFile.__init__(self, filename, record, blocking_factor, empty_key)

    def init_file(self):
        with open(self.filename, "wb") as f:
            block = self.blocking_factor*[self.get_empty_rec()]
            self.write_block(f, block)

    def init_file_aktivna_datoteka(self):
        with open(self.filename, "wb") as f:
            block = self.blocking_factor*[{"id": self.empty_key, "ime_i_prezime": "", "datum_i_vreme": "", "oznaka_spasioca":"","trajanje_spasavanja":0,"status": 0}]
            self.write_block(f, block)

    def init_file_datoteka_gresaka(self):
        with open(self.filename, "wb") as f:
            block = self.blocking_factor*[{"id": self.empty_key, "opis_greske": ""}]
            self.write_block(f, block)

    def __find_in_block(self, block, rec):
        for j in range(self.blocking_factor):
            if block[j].get("id") == self.empty_key or block[j].get("id") > rec.get("id"):
                return (True, j)

        return (False, None)

    def insert_record(self, rec):
        if self.find_by_id(rec.get("id")):
            print("Already exists with ID {}".format(rec.get("id")))
            return

        with open(self.filename, "rb+") as f:
            while True:
                block = self.read_block(f)

                if not block:           # EOF
                    break

                last = self.__is_last(block)
                here, j = self.__find_in_block(block, rec)

                if not here:
                    continue

                # save last record for inserting into next block
                tmp_rec = block[self.blocking_factor-1]
                for k in range(self.blocking_factor-1, j, -1):
                    block[k] = block[k-1]               # move records
                block[j] = rec                          # insert
                rec = tmp_rec                           # new record for insertion

                f.seek(-self.block_size, 1)
                self.write_block(f, block)

                # last block without empty rec?
                if last and block[self.blocking_factor-1].get("id") != self.empty_key:
                    block = self.blocking_factor*[self.get_empty_rec()]
                    self.write_block(f, block)

    def kopiranje(self, aktivna):
        with open(aktivna.filename, "rb") as f:
            self.insert_record(aktivna.read_record(f))


    def insert_record_no_id_check(self,rec):
        with open(self.filename, "rb+") as f:
            while True:
                block = self.read_block(f)

                if not block:           # EOF
                    break

                last = self.__is_last(block)
                here, j = self.__find_in_block(block, rec)

                if not here:
                    continue

                # save last record for inserting into next block
                tmp_rec = block[self.blocking_factor-1]
                for k in range(self.blocking_factor-1, j, -1):
                    block[k] = block[k-1]               # move records
                block[j] = rec                          # insert
                rec = tmp_rec                           # new record for insertion

                f.seek(-self.block_size, 1)
                self.write_block(f, block)

                # last block without empty rec?
                if last and block[self.blocking_factor-1].get("id") != self.empty_key:
                    block = self.blocking_factor*[self.get_empty_rec()]
                    self.write_block(f, block)

    def __is_last(self, block):
        for i in range(self.blocking_factor):
            if block[i].get("id") == self.empty_key:
                return True
        return False

    def print_file(self):
        i = 0
        with open(self.filename, "rb") as f:
            while True:
                block = self.read_block(f)

                if not block:
                    break

                i += 1
                print("Block {}".format(i) + " Broj bloka "+ i)
                self.print_block(block)

    def find_by_id(self, id):
        i = 0
        with open(self.filename, "rb") as f:
            while True:
                block = self.read_block(f)

                if not block:
                    return None

                for j in range(self.blocking_factor):
                    if block[j].get("id") == id:
                        return (i, j)
                    if block[j].get("id") > id:
                        return None

                i += 1

    def mergovanje_izlazne_aktivne(self, aktivna,error):
        br = 0
        with open(self.filename, "rb+") as f:
            temp = self.read_record(f)
            if temp["svrha"] == 1:
                if aktivna.find_by_id(temp["id"]) is not None:
                    br+=1
                    error.insert_record({"id":br,"opis_greske":"Vec postoji sa tim evidencionim brojem"})
                else:
                    aktivna.insert_record(temp)
            elif temp["svrha"] == 2:
                if aktivna.find_by_id(temp["id"]) is None:
                    br+=1
                    error.insert_record({"id": br, "opis_greske": "Ne postoji spasavanje sa tim evidencionim brojem"})
                else:
                    aktivna.change_by_id(temp)
            elif temp["svrha"] == 3:
                if aktivna.find_by_id(temp["id"]) is None:
                    br += 1
                    error.insert_record({"id": br, "opis_greske": "Ne postoji spasavanje sa tim evidencionim brojem"})
                else:
                    aktivna.logical_delete_by_id(temp)
            elif temp["svrha"] == 4:
                if aktivna.find_by_id(temp["id"]) is None:
                    br += 1
                    error.insert_record({"id": br, "opis_greske": "Ne postoji spasavanje sa tim evidencionim brojem"})
                else:
                    aktivna.delete_by_id(temp["id"])


    def change_by_id(self, promena):
        found = self.find_by_id(promena["id"])
        if not found:
            return 0
        block_idx = found[0]
        rec_idx = found[1]
        with open(self.filename, "rb+") as f:
            f.seek(block_idx * self.block_size)
            block = self.read_block(f)
            temp = block[rec_idx]
            #print(temp)
            if promena["ime_i_prezime"] !="":
                temp["ime_i_prezime"] = promena["ime_i_prezime"]
            if promena["datum_i_vreme"] !="":
                temp["datum_i_vreme"] = promena["datum_i_vreme"]
            if promena["oznaka_spasioca"]!="":
                temp["oznaka_spasioca"] = promena["oznaka_spasioca"]
            if promena["trajanje_spasavanja"] != -1:
                temp["trajanje_spasavanja"] = promena["trajanje_spasavanja"]

            f.seek(-1 * self.block_size, 1)
            self.write_block(f, block)

    def logical_delete_by_id(self,promena):
        found = self.find_by_id(promena["id"])
        if not found:
            return 0
        block_idx = found[0]
        rec_idx = found[1]
        with open(self.filename, "rb+") as f:
            f.seek(block_idx * self.block_size)
            block = self.read_block(f)
            temp = block[rec_idx]
            temp["status"] = 0
            f.seek(-1 * self.block_size, 1)
            self.write_block(f, block)

    def delete_by_id(self, id):
        found = self.find_by_id(id)

        if not found:
            return

        block_idx = found[0]
        rec_idx = found[1]
        next_block = None

        with open(self.filename, "rb+") as f:
            while True:
                f.seek(block_idx * self.block_size)  # last block
                block = self.read_block(f)

                for i in range(rec_idx, self.blocking_factor-1):
                    block[i] = block[i+1]       # move records

                if self.__is_last(block):              # is last block full?
                    f.seek(-self.block_size, 1)
                    self.write_block(f, block)
                    break

                next_block = self.read_block(f)
                # first record of next block is now the last of current one
                block[self.blocking_factor-1] = next_block[0]
                f.seek(-2*self.block_size, 1)
                self.write_block(f, block)

                block_idx += 1
                rec_idx = 0

        if next_block and next_block[0].get("id") == self.empty_key:
            os.ftruncate(os.open(self.filename, os.O_RDWR),
                         block_idx * self.block_size)
