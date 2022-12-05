import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd


def download_data(ticker: str,
                  start_date: datetime = None,
                  end_date: datetime = None) -> tuple((yf.ticker.Ticker, pd.DataFrame)):

    tick = yf.Ticker(ticker)
    if start_date is None and end_date is None:
        tick_data = tick.history(period='max')
    else:
        tick_data = tick.history(start=start_date, end=end_date)

    return tick, tick_data


if __name__ == '__main__':
    tick, data = download_data('GOOGL')

