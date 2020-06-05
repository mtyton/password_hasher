from peewee import Model, CharField
from peewee import SqliteDatabase

db = SqliteDatabase('passwords.db')


class Password(Model):
    website_name = CharField(120, unique=True)
    password = CharField(255)

    class Meta:
        database = db

    def create_tab(self):
        self.create_table(Password)

    @staticmethod
    def get_website_names():
        passwords = Password.select()
        websites = []
        for p in passwords:
            websites.append(p.website_name)
        return websites


class KeyPair(Model):
    key_password = CharField(255, unique=True)
    public_key = CharField(255, unique=True)
    private_key = CharField(255, unique=True)

    def save_key_pair(self, password, public_key, private_key):
        pass

    def get_key_pair(self):
        pass