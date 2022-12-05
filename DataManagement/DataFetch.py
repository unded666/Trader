import yfinance as yf
from datetime import datetime
import pandas as pd


def download_data(ticker: str,
                  start_date: datetime,
                  end_date: datetime) -> tuple(yf.ticker.Ticker, pd.DataFrame):

    tick = yf.Ticker(ticker)
    tick_data = tick.history(period='max')

    return tick, tick_data


if __name__ == '__main__':
    print('I am debugging code, hear me roar')
