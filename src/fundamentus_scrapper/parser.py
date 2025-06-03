from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import pandas as pd

def get_page_soup(url: str) -> BeautifulSoup:
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url,headers=hdr)
    page = urlopen(req)
    return BeautifulSoup(page)

def get_table_from_soup(soup: BeautifulSoup) -> pd.DataFrame:
  table = soup.find('table')

  rows = []
  for tr in table.find_all('tr'):
      cells = [td.get_text(strip=True) for td in tr.find_all(['th', 'td'])]
      rows.append(cells)

  header = rows[0]
  data = rows[1:]

  return pd.DataFrame(data, columns=header)
  
def extract_table_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table")
    df = pd.read_html(str(table))[0]
    return df
