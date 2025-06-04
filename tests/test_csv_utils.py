from pathlib import Path
import pandas as pd
from scrapper.csv_utils import save_page_table_csv, load_csv

def test_save_and_load_csv():
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)

    csv_path = data_dir / "stocks.csv"
    save_page_table_csv(str(csv_path))
    df = load_csv(str(csv_path))
    assert isinstance(df, pd.DataFrame)
    assert not df.empty