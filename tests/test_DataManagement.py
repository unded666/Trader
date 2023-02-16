from unittest import TestCase
import pandas as pd
import os
from DataManagement.DataFetch import download_data
from DataManagement.DataManagement import (save_data,
                                           load_data,
                                           DataCombinator)

for path, _, files in os.walk(os.getcwd()):
    if 'read_this.pkl' in files:
        TGT_LOCATION  = path

TGT_READ_FIL = "read_this.pkl"
TGT_WRITE_FIL = "write_this.pkl"
TEST_TICKER = 'GOOG'


class DManTest(TestCase):
    """
    tests for the data management class
    """

    def setUp(self) -> None:
        """
        creates a default set of read and write target locations, plus a consistent
        dataframe to test the DataManagement functions
        """
        self.read_target = f"{TGT_LOCATION}\\{TGT_READ_FIL}"
        self.write_target = f"{TGT_LOCATION}\\{TGT_WRITE_FIL}"
        self.location = TGT_LOCATION
        self.dummy_df = pd.DataFrame({'cats': [1], 'dogs': [0], 'bunnies': [72]})
        self.combinator = DataCombinator()
        self.ticker, self.frame, _ = download_data(TEST_TICKER)


    def test_save_data(self):
        """
        tests the operation of the save_data method by removing the saved target file, writing
        a new file and verifying the new written file
        """

        if os.path.basename(self.write_target) in os.listdir(self.location):
            # clear target file
            os.remove(self.write_target)
        self.assertFalse(os.path.basename(self.write_target) in os.listdir(self.location),
                         f"test file not correctly deleted")
        save_data(self.write_target, self.dummy_df)
        location_files = os.listdir(self.location)
        self.assertTrue(os.path.basename(self.write_target) in location_files, f"test file not correctly written")

    def test_load_data(self):
        """
        Tests the operation of the load_data method by loading in a known file and verifying the
        data found within.
        """

        loaded_data = load_data(self.read_target)
        rows, cols = loaded_data.shape
        expected_rows = 4609
        expected_cols = 7
        self.assertEqual(rows, expected_rows, f"incorrect data read in, expected {expected_rows} rows, got {rows}")
        self.assertEqual(cols, expected_cols, f"incorrect data read in, expected {expected_cols} rows, got {cols}")

    def test_reshape_data(self):
        """
        Tests the operation of reshape_data by creating a new dataframe using the reshape_data method,
        and verifying the new dataframe has an extra column, no new or lost rows, and that the new
        dataframe has an appropriately named 'Ticker' column
        """

        out_frame = self.combinator.reshape_data(self.ticker, self.frame)
        self.assertEqual(self.frame.shape[1], out_frame.shape[1]-1, 'columns inconsistent when adding ticker')
        self.assertEqual(self.frame.shape[0], out_frame.shape[0], 'data rows inconsistent when reshaping frame')
        self.assertTrue('Ticker' in out_frame.columns, 'missing Ticker column for new dataframe')
