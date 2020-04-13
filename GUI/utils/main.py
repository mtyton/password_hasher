from GUI.utils.hasher import Hasher
from GUI.utils.keyes import EnKeyes
from GUI.utils.db import Password
from peewee import IntegrityError

AVAILABLE_COMMANDS = ["read", "save", "update", "check", "copy"]


def save(password, website, encryptor, public_key):
    if not website or not password:
        return False
    new_pass = encryptor.encrypt_with_public_key(password, public_key)
    try:
        encryptor.save_password(new_pass, website)
    except IntegrityError:
        print("password already in db, updating")
        encryptor.update_password(website, new_pass)
    print("saved password")
    return True


def read(website, encryptor, private_key):
    old_pass = encryptor.read_password(website)
    new_pass = encryptor.decrypt_with_private_key(old_pass, private_key)
    return new_pass


def update():
    pass


def get_keys(encryptor):
    if not EnKeyes.check_if_key_exists():
        pr_numb, sec_pr_numb = encryptor.find_primal_numbs()
        en_key = EnKeyes(pr_numb, sec_pr_numb)
        en_key.generate_keys()
        private_key, public_key = en_key.get_keys()
        en_key.save_keys(public_key, private_key)
        print("created key")
    else:
        print("reading keys")
        private_key, public_key = EnKeyes.read_keys()
    return private_key, public_key


def excute(command, get_web, get_pass):
    website = get_web()

    assert(command in AVAILABLE_COMMANDS)
    encryptor = Hasher()
    private_key, public_key = get_keys(encryptor)
    if command == "save":
        password = get_pass()
        if password:
            result = save(password, website, encryptor, public_key)
            if not result:
                raise ValueError("you have too pass all values")
    elif command == "get":
        result = read(website, encryptor, private_key)
        print(result)
    elif command == "copy":
        result = read(website, encryptor, private_key)

    return result