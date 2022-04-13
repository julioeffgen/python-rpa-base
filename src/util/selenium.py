from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.variables import chrome_driver_path, firefox_driver_path
from src.database.rpa import update_error_status
from src.exception.base import RpaException
from src.util.logger import log


def create_chrome_instance(db_connection, record, download_path):
    chrome_options = Options()
    chrome_options.add_argument("--lang=pt-BR")
    chrome_options.add_experimental_option('prefs', {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    }
                                           )
    try:
        return webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    except Exception as ex:
        update_error_status(ex, db_connection, record, 'Error on create driver instance', 'chrome_driver_error')
        raise RpaException('Error on create ChromeDriver')


def create_firefox_instance(record, db_connection):
    try:
        driver = webdriver.Firefox(executable_path=firefox_driver_path)
        driver.maximize_window()
        return driver
    except Exception as ex:
        update_error_status(ex, db_connection, record, 'Error on create driver instance', 'firefox_driver_error')
        raise RpaException('Error on create FireFoxDriver')


def open_uri(driver, url):
    try:
        driver.get(url)
    except Exception as e:
        log(e)
        raise RpaException(f'Error on access {url}')
