from pathlib import Path
import pandas as pd
from scrapper.csv_utils import save_page_table_csv, load_csv, save_stocks_page_numeric_table_csv

def get_data_dir():
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir

def test_save_and_load_csv():
    data_dir = get_data_dir()

    csv_path = data_dir / "stocks_raw.csv"
    save_page_table_csv(str(csv_path))
    df = load_csv(str(csv_path))
    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_save_stocks_page_numeric_table_csv():
    data_dir = get_data_dir()

    csv_path = data_dir / "stocks.csv"
    save_stocks_page_numeric_table_csv(str(csv_path))
    df = load_csv(str(csv_path))
    assert isinstance(df, pd.DataFrame)
    assert not df.empty