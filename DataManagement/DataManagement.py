import pandas as pd
import pickle
from yfinance import Ticker


def save_data(target: str, data: pd.DataFrame) -> None:
    """
    saves a pickled dataframe to the target file. Pickled as opposed to a csv save
    in order to preserve types within the dataframe should they exist.

    :param target: target file of the format directory/filename
    :param data: pandas dataframe
    :return: None
    """

    with open(target, 'wb') as fil:
        pickle.dump(data, fil)


def load_data(target: str) -> pd.DataFrame:
    """
    loads a pickled dataframe from the specified target location and returns an
    unpickled dataframe

    :param target: target file of the format directory/filename
    :return: loaded data
    """

    with open(target, 'rb') as fil:
        df = pickle.load(fil)

    return df


class DataCombinator:

    def __init__(self) -> None:
        """

        """

        pass

    def reshape_data(self, tic: Ticker, history: pd.DataFrame) -> pd.DataFrame:
        """
        takes the historical data from the history dataframe and adds a column
        from the ticker object that has the actual ticker, for use in combining
        data from multiple equities

        :param tic: share information that is not daily price-related
        :param history: dataframe with the actual closing prices of shares
        :return: dataframe with the necessary additions
        """

        return None

    def add_new_data_to_historical(self,
                                   historical: pd.DataFrame,
                                   new_tic: Ticker,
                                   new_history: pd.DataFrame) -> pd.DataFrame:
        """
        reshapes the new historical data new_history using the ticker object new_tic,
        which is then appended on to the data in historical, returning the combined dataframe

        :param historical: dataframe with a new stock's prices
        :param new_tic: Ticker object with descriptive information about the new data
        :param new_history: existing historical data
        :return: combined dataframe
        """

        return None
