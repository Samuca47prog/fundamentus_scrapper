from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from fundamentus_scrapper.parser import get_page_soup, get_table_from_soup


# get_page_soup tests

@patch("fundamentus_scrapper.parser.urlopen")
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
