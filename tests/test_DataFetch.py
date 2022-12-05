from unittest import TestCase
from datetime import datetime, timedelta
from DataManagement.DataFetch import download_data

TEST_TICKERS = ['GOOGL', 'AAPL', 'MSFT', 'ULVR.L']


class DataTest(TestCase):

    def test_download(self) -> None:
        """
        tests the download functionality. Downloads only the last week's worth of data from
        each tests ticker. Runs the following tests:
        - Tests a 1-week download for each tests ticker
        - Tests a maximum history download for microsoft

        :return: Nothing
        """
        dt_today = datetime.now()
        dt_from = dt_today - timedelta(days=7)
        #results = {ticker: [Tick, Tick.history(start=dt_today, end=dt_from)] for ticker in TEST_TICKERS}
        results = {}
        for ticker in TEST_TICKERS:
            _, Tick_data = download_data(ticker, start_date=dt_from, end_date=dt_today)
            self.assertGreater(Tick_data.shape[0], 0, f"no data downloaded for {ticker} for a 1-week period")
        _, Tick_data = download_data(TEST_TICKERS[2])
        self.assertGreater(Tick_data.shape[0], 0, f"maximum time download failed for {TEST_TICKERS[2]}")

