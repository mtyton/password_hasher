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
