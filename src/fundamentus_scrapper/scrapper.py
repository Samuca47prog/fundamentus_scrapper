from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import src.config

def get_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def apply_filters(driver, filters):
    driver.get("https://www.fundamentus.com.br/buscaavancada.php")
    time.sleep(2)

    for key, value in filters.items():
        try:
            field = driver.find_element(By.NAME, key)
            field.clear()
            field.send_keys(str(value))
        except Exception as e:
            print(f"Filter {key} not found: {e}")

    driver.find_element(By.NAME, "buscar").click()

def extract_table_html(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )
    return driver.page_source
