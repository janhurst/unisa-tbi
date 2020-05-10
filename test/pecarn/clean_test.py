import unittest
import pandas as pd

# hack for PYTHONPATH issues
import os, sys
sys.path.append(os.path.abspath('./src'))
from data import pecarn

class CleanTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pecarn.clean(pecarn.load(fromCsv=True))

    def test_clean_returns_dataframe(self):
        self.assertIsInstance(self.df, pd.DataFrame)

    def test_clean_variable_count(self):
        self.assertEqual(self.df.shape[1], 67)

    def test_no_nans(self):
        self.assertEqual(self.df.isna().sum().sum(), 0)

if __name__ == '__main__':
    unittest.main()