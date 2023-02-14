from unittest import TestCase
import pandas as pd
import os
from DataManagement.DataFetch import download_data
from DataManagement.DataManagement import (save_data,
                                           load_data,
                                           DataCombinator)

TGT_LOCATION = '\\test_files'
TGT_READ_FIL = '\\test_files/read_this.pkl'
TGT_WRITE_FIL = '\\test_files/write_this.pkl'
TEST_TICKER = 'GOOG'


class DManTest(TestCase):
    """
    tests for the data management class
    """

    def setUp(self) -> None:

        cwd = os.getcwd()
        self.read_target = f"{cwd}{TGT_READ_FIL}"
        self.write_target = f"{cwd}{TGT_WRITE_FIL}"
        self.location = f"{cwd}{TGT_LOCATION}"
        self.dummy_df = pd.DataFrame({'cats': [1], 'dogs': [0], 'bunnies': [72]})
        self.combinator = DataCombinator()
        self.ticker, self.frame, _ = download_data(TEST_TICKER)


    def test_save_data(self):

        if os.path.basename(self.write_target) in os.listdir(self.location):
            # clear target file
            os.remove(self.write_target)
        self.assertFalse(os.path.basename(self.write_target) in os.listdir(self.location),
                         f"test file not correctly deleted")
        save_data(self.write_target, self.dummy_df)
        files = os.listdir(self.location)
        self.assertTrue(os.path.basename(self.write_target) in files, f"test file not correctly written")

    def test_load_data(self):

        loaded_data = load_data(self.read_target)
        rows, cols = loaded_data.shape
        expected_rows = 4609
        expected_cols = 7
        self.assertEqual(rows, expected_rows, f"incorrect data read in, expected {expected_rows} rows, got {rows}")
        self.assertEqual(cols, expected_cols, f"incorrect data read in, expected {expected_cols} rows, got {cols}")

    def test_reshape_data(self):

        out_frame = self.combinator.reshape_data(self.ticker, self.frame)
        self.assertEqual(self.frame.shape[1], out_frame.shape[1]-1, 'columns inconsistent when adding ticker')
        self.assertEqual(self.frame.shape[0], out_frame.shape[0], 'data rows inconsistent when reshaping frame')
        self.assertTrue('Ticker' in out_frame.columns, 'missing Ticker column for new dataframe')
