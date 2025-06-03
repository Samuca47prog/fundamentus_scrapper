from .scrapper import get_driver, apply_filters, extract_table_html
from .parser import extract_table_from_html
from . import config


def main() -> None:
    """Entry point for the command line script."""

    driver = get_driver(headless=False)
    try:
        apply_filters(driver, config.FILTERS)
        html = extract_table_html(driver)
        df = extract_table_from_html(html)
        print(df.head())
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
