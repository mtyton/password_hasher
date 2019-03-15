import argparse
from hasher import Hasher
from keyes import EnKeyes
from db import Password

def save(args, password):
    password = password
    has = Hasher()
    new_pass = has.encrypt(password=password)
    print(new_pass)
    #has.save_password(new_pass, args.website)

def read(source):
    has = Hasher()
    old_pass = has.decrypt("rak")
    print(old_pass)


if __name__ == '__main__':
    p = Password()
    hash = Hasher()
    parser = argparse.ArgumentParser(description="say if you like to get or set password")
    parser.add_argument('action', metavar="A", type=str, help="Give GET or SAVE to choose which action u want to do")
    parser.add_argument('website', metavar="S", type=str, help="to which portal you want to save your password"
                                                               "(important while getting it back)")

    if not EnKeyes.check_if_key_exists():
        pr_numb, sec_pr_numb = hash.find_primal_numbs()
        en_key = EnKeyes(pr_numb, sec_pr_numb)
        en_key.generate_keys()
        private_key, public_key = en_key.get_keys()
        en_key.save_keys(public_key, private_key)
        print("created key")
    else:
        print("reading keys")
        private_key, public_key = EnKeyes.read_keys()

    args = parser.parse_args()
    if args.action == "save":
        password = input("Give your password:")
        new_word = hash.encrypt_with_public_key(password, public_key)
        hash.save_password(new_word, args.website)

    elif args.action == "get":
        readed = hash.read_password(args.website)
        hash.decrypt_with_private_key(readed, private_key)