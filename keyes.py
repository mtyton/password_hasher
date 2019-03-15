from random import random
from random import randrange
import os

class EnKeyes:
    def __init__(self, pr_numb, sec_pr_numb):
        self.pr_numb = pr_numb
        self.sec_pr_numb = sec_pr_numb
        self.private_key = []
        self.public_key = []

    def generate_keys(self):
        module = self.get_module()
        co_numb, fi_numb = self.coprime()
        reversed_modulo = self.reverse_modulo(fi_numb, co_numb)
        if reversed_modulo is None:
            raise ValueError("no reversed modulo")
        self.create_private_key(co_numb, module)
        self.create_public_key(reversed_modulo, module)
        #need module, co_numb, and d

    def coprime(self):
        module = self.get_module()
        fi_numb = self.get_Euler_func()
        co_prime_numb = 505
        while self.nwd(fi_numb, co_prime_numb) != 1:
            co_prime_numb += 2
            if co_prime_numb % 2 == 0:
                co_prime_numb += 1
            co_factors = self.to_prime_factors(co_prime_numb)
        return co_prime_numb, fi_numb

    def to_prime_factors(self, numb):
        iterator = 2
        factors = []
        while numb > 1:
            if numb%iterator == 0:
                factors.append(iterator)
                numb /= iterator
            elif numb%iterator != 0:
                iterator += 1
        return factors

    def check_comprimality(self, fi_factors, numb_factors):
        for factor in fi_factors:
            if factor in numb_factors:
                return False
        return True

    def get_Euler_func(self):
        fi_numb = (self.pr_numb-1)*(self.sec_pr_numb-1)
        return fi_numb

    def get_module(self):
        module = self.pr_numb * self.sec_pr_numb
        return module

    def nwd(self,a, b):
        while b:
            a, b = b, a % b
        return a

    def reverse_modulo(self, a, b):
        for i in range(2, a):
            if i*b % a == 1:
                return i
        return None

    def create_private_key(self, numb, module):
        self.private_key = [numb, module]

    def create_public_key(self, reversed_modulo, module):
        self.public_key = [reversed_modulo, module]

    def get_keys(self):
        return self.private_key, self.public_key

    def save_keys(self, public_key, private_key):
        file = open("keys.txt", "w")
        file.write("{} {} ".format(public_key[0], public_key[1]))
        file.write("\n")
        file.write("{} {} ".format(private_key[0], private_key[1]))
        file.close()

    @staticmethod
    def read_keys():
        file = open("keys.txt", "r")
        line = file.readline().split(" ")
        public = [int(line[0]), int(line[1])]
        line = file.readline().split(" ")
        private = [int(line[0]), int(line[1])]
        file.close()
        return private, public

    @staticmethod
    def check_if_key_exists():
        file_checker = os.path.isfile("keys.txt")
        if file_checker:
            return True
        else:
            return False