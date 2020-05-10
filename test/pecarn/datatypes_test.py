import unittest
import pandas as pd

# hack for PYTHONPATH issues
import os, sys
sys.path.append(os.path.abspath('./src'))
from data import pecarn

class DataTypesTestCase(unittest.TestCase):

    boolean_cols = ['Seiz','ActNorm','Vomit','Dizzy','Intubated','Paralyzed','Sedated','AMS',
        'FontBulg','SFxBas','Hema','Clav','NeuroD','OSI','Drugs','PosIntFinal']

    categorical_cols = ['Amnesia_verb','LOCSeparate','HA_verb','SFxPalp','InjuryMech','LocLen',
        'SeizOccur','SeizLen','HASeverity','HAStart','VomitNbr','VomitStart','GCSEye','GCSVerbal',
        'GCSMotor','GCSGroup','HemaLoc','HemaSize','AgeTwoPlus','Gender','Ethnicity','Race']

    numeric_cols = ['AgeInMonth','AgeinYears','GCSTotal']

    @classmethod
    def setUpClass(cls):
        cls.df = pecarn.load(fromCsv=True)

    def test_Booleans(self):
        self.boolean_cols.sort()
        for col in self.boolean_cols:
            with self.subTest(name=col):
                self.assertIsInstance(self.df[col].dtype, pd.BooleanDtype)

    def test_Categorical(self):
        self.categorical_cols.sort()
        for col in self.categorical_cols:
            with self.subTest(name=col):
                self.assertIsInstance(self.df[col].dtype, pd.CategoricalDtype)

    def test_numeric(self):
        self.numeric_cols.sort()
        for col in self.numeric_cols:
            with self.subTest(name=col):
                self.assertIsInstance(self.df[col].dtype, pd.Int64Dtype)


if __name__ == '__main__':
    unittest.main()