from src.scrapper import get_driver, apply_filters, extract_table_html
from src.parser import extract_table_from_html
import src.config as config

def main():
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
