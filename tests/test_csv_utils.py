import pytest

from pathlib import Path
import pandas as pd

from scrapper.csv_utils import save_page_table_csv, load_csv, save_stocks_page_numeric_table_csv

@pytest.mark.skip(reason="Disabled due to network and no need to update the file")
def test_save_and_load_csv(get_data_dir):
    csv_path = get_data_dir / "stocks_raw.csv"
    save_page_table_csv(str(csv_path))
    df = load_csv(str(csv_path))
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

@pytest.mark.skip(reason="Disabled due to network and no need to update the file")
def test_save_stocks_page_numeric_table_csv(get_data_dir):
    csv_path = get_data_dir / "stocks.csv"
    save_stocks_page_numeric_table_csv(str(csv_path))
    df = load_csv(str(csv_path))
    assert isinstance(df, pd.DataFrame)
    assert not df.empty