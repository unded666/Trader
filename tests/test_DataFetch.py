from unittest import TestCase
from datetime import datetime, timedelta
from DataManagement.DataFetch import (download_data,
                                      download_economic_data)


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
        """
        dt_today = datetime.now()
        dt_from = dt_today - timedelta(days=7)
        for ticker in TEST_TICKERS:
            _, tick_data, found = download_data(ticker, start_date=dt_from, end_date=dt_today)
            self.assertGreater(tick_data.shape[0], 0, f"no data downloaded for {ticker} for a 1-week period")
            self.assertTrue(found, f"download flag for {ticker} incorrectly flagged as {found}")
        _, tick_data, _ = download_data(TEST_TICKERS[2])
        self.assertGreater(tick_data.shape[0], 0, f"maximum time download failed for {TEST_TICKERS[2]}")
        _, _, found = download_data('NOT_A_TICKER')
        self.assertFalse(found, f"false ticker incorrectly returned {found}")

    def test_download_economic_data(self) -> None:
        """
        Tests that the economic downloads from the world bank api work as intended.
        Tests the following:
        - USA data downloaded
        - GBR data downloaded
        - working age population is downloaded correctly
        - pricing parity GDP is downloaded correctly
        - gdp growth % is downloaded and renamed correctly
        """

        eco_df = download_economic_data()
        self.assertGreater(eco_df.shape[0], 0, f"no data downloaded from wbgapi")
        economies = ['GBR', 'USA']
        downloaded_economies = list(eco_df.economy.unique())
        for eco in economies:
            self.assertTrue(eco in downloaded_economies, f"{eco} not downloaded from wbgapi")
        features = list(eco_df.columns)
        for feature in ['GDP (PPP-2017)', 'Population (working age)', 'GDP growth (annual %)']:
            self.assertTrue(feature in features, f"{feature} not downloaded")
