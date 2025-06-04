import pandas as pd

from .parser import get_page_soup, get_table_from_soup, convert_to_numeric_columns
from config import STOCKS_CONFIG


def save_page_table_csv(path: str, url: str="https://www.fundamentus.com.br/resultado.php") -> None:
    """Fetch the stocks table from Fundamentus and save it as CSV.

    Parameters
    ----------
    path:
        Destination file path for the CSV.
    """
    soup = get_page_soup(url)
    df = get_table_from_soup(soup)
    df.to_csv(path, index=False)

def save_stocks_page_numeric_table_csv(path: str) -> None:
    """Fetch the stocks table from Fundamentus, convert it to numeric and save it as CSV.

    Parameters
    ----------
    path:
        Destination file path for the CSV.
    """
    soup = get_page_soup("https://www.fundamentus.com.br/resultado.php")
    df = get_table_from_soup(soup)
    df = convert_to_numeric_columns(df, STOCKS_CONFIG)
    df.to_csv(path, index=False)

def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file into a :class:`pandas.DataFrame`."""
    return pd.read_csv(path)