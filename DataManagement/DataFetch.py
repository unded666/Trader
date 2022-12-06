import yfinance as yf
from datetime import datetime
import pandas as pd
import wbgapi as wb


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


def download_economic_data() -> pd.DataFrame:
    """

    :return:
    """
    gdp_ppp = 'NY.GDP.MKTP.PP.KD'
    gdp_growth = 'NY.GDP.MKTP.KD.ZG'
    working_population = 'SP.POP.1564.TO'
    country_uk = 'GBR'
    country_usa = 'USA'

    df = wb.data.DataFrame([gdp_ppp, gdp_growth, working_population], [country_usa, country_uk],
                           columns='series', numericTimeKeys=True).reset_index()
    translator = {gdp_ppp: 'GDP (PPP-2017)',
                  gdp_growth: 'GDP growth (annual %)',
                  working_population: 'Population (working age)'}
    df = df.rename(columns=translator)

    return df


if __name__ == '__main__':
    pass
