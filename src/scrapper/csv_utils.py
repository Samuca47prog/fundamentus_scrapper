import pandas as pd

from .parser import get_page_soup, get_table_from_soup


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


def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file into a :class:`pandas.DataFrame`."""
    return pd.read_csv(path)