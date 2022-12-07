import pandas as pd
import pickle

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
