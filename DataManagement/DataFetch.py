import yfinance as yf
from datetime import datetime
import pandas as pd


def download_data(ticker: str,
                  start_date: datetime = None,
                  end_date: datetime = None) -> tuple[yf.ticker.Ticker, pd.DataFrame, bool]:
    """
    downloads the requested data from yahoo finance. The ticker is expected to be correct,
    but will return an empty dataframe if it is incorrect.

    :param ticker: text ticker of quoted stock
    :param start_date: datetime object of start date
    :param end_date: datetime object of end date
    :return: ticker object, history dataframe, data found flag
    """

    download_tick = yf.Ticker(ticker)
    found = True
    if start_date is None and end_date is None:
        tick_data = download_tick.history(period='max')
    else:
        tick_data = download_tick.history(start=start_date, end=end_date)
    if tick_data.shape[0] == 0:
        found = False

    return download_tick, tick_data, found


if __name__ == '__main__':
    pass
