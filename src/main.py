from scrapper.parser import (
    get_page_soup,
    get_table_from_soup,
    convert_to_numeric_columns,
)
from config import STOCKS_CONFIG
from gui.tk_app import run


def main() -> None:
    """Entry point for the command line script."""

    soup = get_page_soup("https://www.fundamentus.com.br/resultado.php")
    df = get_table_from_soup(soup)
    df = convert_to_numeric_columns(df, STOCKS_CONFIG)

    run(df)


if __name__ == "__main__":
    main()
