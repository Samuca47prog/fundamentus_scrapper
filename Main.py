from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # only needed if not using a fixed path

def open_fundamentus():
    # Optional: run Chrome headless (in background)
    options = Options()
    # options.add_argument("--headless")  # Uncomment if you want no GUI
    options.add_argument("--start-maximized")

    # Option 1: Use ChromeDriver path manually (if you downloaded and set it yourself)
    # service = Service("C:/tools/chromedriver.exe")
    # driver = webdriver.Chrome(service=service, options=options)

    # Option 2: Use webdriver-manager to auto-download the right driver version
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the site
    url = "https://www.fundamentus.com.br/"
    driver.get(url)

    # Optional: Wait so you can see the page
    input("Press Enter to close the browser...")

    # Close browser
    driver.quit()

if __name__ == "__main__":
    open_fundamentus()
