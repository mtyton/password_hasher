import base64
import os
from random import randrange
from passlib.hash import sha256_crypt
from Crypto.Cipher import AES
from peewee import SqliteDatabase
from db import Password
from primal import Rabin_Miller
from random import random

db = SqliteDatabase('passwords.db')
db.connect()
db.create_tables([Password], safe=True)


class Hasher:
    def __init__(self):
        self.cipher = AES.new("longtermpassword".encode("utf-8"), AES.MODE_ECB)

    def find_primal_numbs(self):
        pr_numb = int(randrange(3, 500))  # pr_numb - primal_number
        rab = Rabin_Miller(pr_numb, 10)
        while not rab.check():
            pr_numb = int(randrange(2, 500))
            rab.change_number(pr_numb)

        sec_pr_numb = int(randrange(2, 500))
        rab.change_number(sec_pr_numb)
        while not rab.check():
            sec_pr_numb = int(randrange(2, 500))
            rab.change_number(sec_pr_numb)

        return pr_numb, sec_pr_numb

    def encrypt_with_public_key(self, password, key):
        new_word = []
        for p in password:
            char = ord(p)
            char = char**key[0] % key[1]
            new_word.append(char)
        return new_word

    def decrypt_with_private_key(self, password, key):
        new_word = ""
        for p in password:
            try:
                t = int(p)**key[0] % key[1]
                char = chr(t)
                new_word += char
            except ValueError:
                pass
        print(new_word)

    def save_password(self, hashed_password, website):
        p = Password()
        p.website_name = website
        p.password = ""
        for h in hashed_password:
            p.password += "{}_".format(h)
        print(p.password)
        p.save()

    def read_password(self, website):
        p = Password.select().where(Password.website_name == website)
        # print(p[0].password)
        arrayed_pass = p[0].password.split("_")
        return arrayed_pass