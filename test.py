import unittest
from primal import Rabin_Miller


class TestRabinMiller(unittest.TestCase):

    def test_check_number(self):
        rab = Rabin_Miller(13, 20)
        print(rab.check())