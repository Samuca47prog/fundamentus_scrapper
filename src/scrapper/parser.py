from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import pandas as pd

from config import STOCKS_CONFIG

def get_page_soup(url: str) -> BeautifulSoup:
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url,headers=hdr)
    page = urlopen(req)
    return BeautifulSoup(page, features="html.parser")

def get_table_from_soup(soup: BeautifulSoup) -> pd.DataFrame:
  table = soup.find('table')

  rows = []
  for tr in table.find_all('tr'):
      cells = [td.get_text(strip=True) for td in tr.find_all(['th', 'td'])]
      rows.append(cells)

  header = rows[0]
  data = rows[1:]

  return pd.DataFrame(data, columns=header)



def convert_to_numeric_columns(df: pd.DataFrame, metadata: dict) -> pd.DataFrame:
    for col, STOCKS_CONFIG in metadata.items():
        if STOCKS_CONFIG.get("numeric") and STOCKS_CONFIG.get("convert") and col in df.columns:
            # Clean and convert
            df[col] = (
                df[col]
                .astype(str)
                .str.replace('%', '', regex=False)
                .str.replace(',', '#', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace('#', '.', regex=False)
            )
            df[col] = pd.to_numeric(df[col], errors='coerce')

            # If marked as percent, divide by 100
            if STOCKS_CONFIG.get("percent", False):
                df[col] = df[col] / 100
    return df



def extract_table_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table")
    df = pd.read_html(str(table))[0]
    return df
