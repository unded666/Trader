from unittest import TestCase
from datetime import datetime, timedelta
from DataManagement.DataFetch import download_data

TEST_TICKERS = ['GOOG', 'AAPL', 'MSFT', 'ULVR.L']


class DataTest(TestCase):

    def test_download(self) -> None:
        """
        tests the download functionality. Downloads only the last week's worth of data from
        each tests ticker. Runs the following tests:
        - Tests a 1-week download for each tests ticker
        - Tests a maximum history download for microsoft
        - tests if good downloads are correctly found
        - tests if incorrect ticker downloads return the correct errors

        :return: Nothing
        """
        dt_today = datetime.now()
        dt_from = dt_today - timedelta(days=7)
        for ticker in TEST_TICKERS:
            _, Tick_data, found = download_data(ticker, start_date=dt_from, end_date=dt_today)
            self.assertGreater(Tick_data.shape[0], 0, f"no data downloaded for {ticker} for a 1-week period")
            self.assertTrue(found, f"download flag for {ticker} incorrecly flagged as {found}")
        _, Tick_data, _ = download_data(TEST_TICKERS[2])
        self.assertGreater(Tick_data.shape[0], 0, f"maximum time download failed for {TEST_TICKERS[2]}")
        _, _, found = download_data('NOT_A_TICKER')
        self.assertFalse(found, f"false ticker incorrectly returned {found}")


