from bs4 import BeautifulSoup
import pandas as pd

def extract_table_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table")
    df = pd.read_html(str(table))[0]
    return df
