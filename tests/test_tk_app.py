import pytest

from scrapper.csv_utils import load_csv

@pytest.mark.skip(reason="Disabled due to GUI")
def test_stock_app_launch(get_data_dir):
    csv_path = get_data_dir / "stocks.csv"
    df = load_csv(csv_path)
    try:
        import tkinter  # noqa: F401
    except ModuleNotFoundError:
        pytest.skip("tkinter not available")
    from gui.tk_app import StockApp

    app = StockApp(df)
    # update once to make sure widgets are created
    app.mainloop()
    # app.update()
    # app.destroy()