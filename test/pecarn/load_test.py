import unittest
import pandas as pd

# hack for PYTHONPATH issues
import os, sys
sys.path.append(os.path.abspath('./src'))
from data import pecarn

class LoadTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pecarn.load(fromCsv=True)

    def test_fromCsv(self):
        self.assertIsInstance(self.df, pd.DataFrame)

    def test_fromPickle(self):
        self.assertIsInstance(self.df, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()