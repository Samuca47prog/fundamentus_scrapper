import pandas as pd

from filters.filters import apply_filters_df
from scrapper.csv_utils import load_csv


def test_apply_filters_df_basic():
    df = pd.DataFrame({"P/L": [10, -5, 50], "P/VP": [5, 10, 15]})
    filters = [
        {"col": "P/L", "op": ">", "val": 0},
        {"col": "P/L", "op": "<", "val": 40},
        {"col": "P/VP", "op": "<", "val": 12},
    ]
    result = apply_filters_df(df, filters)
    assert result.shape[0] == 1
    assert result["P/L"].iloc[0] == 10


def test_apply_filters_df_stocks_csv(get_data_dir):
    csv_path = get_data_dir / "stocks.csv"
    df = load_csv(csv_path)
    filters = [
        {"col": "P/L", "op": ">", "val": 0},
        {"col": "P/L", "op": "<", "val": 40},
        {"col": "P/VP", "op": "<", "val": 12},
    ]
    result = apply_filters_df(df, filters)
    assert result.shape[0] > 1
    print(df.head())
