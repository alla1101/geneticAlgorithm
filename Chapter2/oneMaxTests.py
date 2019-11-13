import sys
sys.path.append("..")

import datetime
import Library.genetic as genetic
import unittest

class OneMaxTests(unittest.TestCase):
    def test(self,length=100):
        geneset=[0,1]

    def get_fitness(genes):
        return genes.count(1)
        