from unittest.mock import patch, MagicMock
import pytest
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

from scrapper.parser import (
    get_page_soup,
    get_table_from_soup,
    convert_to_numeric_columns,
)
from config import STOCKS_CONFIG


# get_page_soup tests

@patch("scrapper.parser.urlopen")
def test_get_page_soup(mock_urlopen):
    html = b"<html><body><p>Hello</p></body></html>"
    mock_urlopen.return_value = MagicMock(read=lambda: html, __enter__=lambda s: s, __exit__=lambda *args: None)
    soup = get_page_soup("http://example.com")
    assert soup.p.text == "Hello"

def test_get_page_soup_fundamentus_stocks_table():
    soup = get_page_soup("https://www.fundamentus.com.br/resultado.php")
    assert "Resultado da busca" in soup.text



# get_table_from_soup tests

def test_get_table_from_soup():
    html = """
    <table>
        <tr><th>Name</th><th>Age</th></tr>
        <tr><td>Alice</td><td>30</td></tr>
        <tr><td>Bob</td><td>25</td></tr>
    </table>
    """
    soup = BeautifulSoup(html, "html.parser")
    df = get_table_from_soup(soup)
    assert list(df.columns) == ["Name", "Age"]
    assert df.loc[0, "Name"] == "Alice"
    assert df.loc[1, "Age"] == "25"


def test_get_table_from_soup_stocks_table():
    soup = get_page_soup("https://www.fundamentus.com.br/resultado.php")
    df = get_table_from_soup(soup)
    assert df.shape[0] > 0



# convert_to_numeric_columns tests

def test_convert_to_numeric_columns_basic():
    df = pd.DataFrame(
        {
            "P/L": ["10,00", "5,50"],
            "Div.Yield": ["1,23%", "2,35%"],
            "Papel": ["A", "B"],
        }
    )

    converted = convert_to_numeric_columns(df.copy(), STOCKS_CONFIG)

    assert converted["P/L"].tolist() == [10.0, 5.5]
    assert converted["Div.Yield"].tolist() == pytest.approx([0.0123, 0.0235])
    # Columns without numeric conversion remain unchanged
    assert converted["Papel"].tolist() == ["A", "B"]


def test_convert_to_numeric_columns():
    soup = get_page_soup("https://www.fundamentus.com.br/resultado.php")
    df = get_table_from_soup(soup)
    df = convert_to_numeric_columns(df, STOCKS_CONFIG)
    assert df["P/L"].dtype == np.float64