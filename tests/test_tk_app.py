import pytest

from scrapper.csv_utils import load_csv
from gui.tk_app import run

# @pytest.mark.skip(reason="Disabled due to GUI")
# to run this test alone ```poetry run pytest tests/test_tk_app.py -vv -s```
def test_stock_app_launch(get_data_dir):
    csv_path = get_data_dir / "stocks.csv"
    df = load_csv(csv_path)
    try:
        import tkinter  # noqa: F401
    except ModuleNotFoundError:
        pytest.skip("tkinter not available")
    from gui.tk_app import StockApp

    run(df)
