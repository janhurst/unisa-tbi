import unittest
import pandas as pd
import numpy as np

# hack for PYTHONPATH issues
import os, sys
sys.path.append(os.path.abspath('./src'))
from data import pecarn

class ProcessedTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pecarn_clean = pecarn.clean(pecarn.load(fromCsv=True))
        cls.df = pecarn.preprocess(pecarn_clean.drop(columns='PosIntFinal'))

    def test_no_categorical(self):
        self.assertEqual((self.df.dtypes == 'category').sum(), 0)

    def test_no_boolean(self):
        self.assertEqual((self.df.dtypes == 'boolean').sum(), 0)        

    def test_all_float64(self):
        self.assertEqual((self.df.dtypes == 'float64').sum(), 66)        


if __name__ == '__main__':
    unittest.main()