# password_hasher - work in progress
Encrypting and decrypting passwords using RSA algorithm, and peewee library to save them inside the database.
Simple in use, takes paramtere "get" or "save", after that he wile show you the password or save it to the db
# How does it works
  ## Main.py
   ### Checking if encrypting keys exists, if they aren't the program will create them and save in txt file
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
  ### After we parse args
    args = parser.parse_args()
  ### Finally we decide wheter we save or get the password from the database
    if args.action == "save":
        ...

    elif args.action == "get":
        ...
  
  ## I used RSA algorithm to encrypt data:
  more soon...
  
# Work still in progress, TODO list:
- repair error while randing primal numbs
- better way of keeping keyes
- write some tests
- password actualization and checking
