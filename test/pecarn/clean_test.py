import unittest
import pandas as pd

# hack for PYTHONPATH issues
import os, sys
sys.path.append(os.path.abspath('./src'))
from data import pecarn

class CleanTestCase(unittest.TestCase):

    def setUp(self):
        self.df = pecarn.clean(pecarn.load(fromCsv=True))

    def test_clean(self):
        self.assertIsInstance(self.df, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()