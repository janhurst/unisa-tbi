import unittest
import pandas as pd

# hack for PYTHONPATH issues
import os, sys
sys.path.append(os.path.abspath('./src'))
from data import pecarn

class LoadTestCase(unittest.TestCase):

    def test_fromCsv(self):
        df = pecarn.load(fromCsv=True)
        self.assertIsInstance(df, pd.DataFrame)

    def test_fromPickle(self):
        df = pecarn.load(fromCsv=False)
        self.assertIsInstance(df, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()