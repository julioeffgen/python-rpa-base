from datetime import date, datetime
from os import environ

separator = r"/"
core_path = f"{separator}Users{separator}julioeffgen{separator}repos{separator}rpa{separator}python-rpa-base{separator}"
base_path = f"{core_path}{separator}files"
process_path = f"{base_path}{separator}process"
processing_path = f"{base_path}{separator}processing"
processed_path = f"{base_path}{separator}processed"
result_path = f"{base_path}{separator}result"
logs_path = f"{base_path}{separator}log"
captcha_path = f"{base_path}{separator}captcha{separator}image"
captcha_image_path = f"{captcha_path}{separator}{datetime.now().timestamp()}"
pdf_path = f"{base_path}{separator}pdf"
pdf_download_path = f"{pdf_path}{separator}{datetime.now().timestamp()}"
excel_path = f"{base_path}{separator}excel"
excel_download_path = f"{excel_path}{separator}{datetime.now().timestamp()}"

drivers_path = f"{core_path}drivers"
chrome_driver_path = f"{drivers_path}{separator}chromedriver"
firefox_driver_path = f"{drivers_path}{separator}geckodriver"

dbc_username = environ['DBC_USER']
dbc_password = environ['DBC_PWD']
dbc_token = environ['DBC_TOKEN']
dbc_percent = "0.3"

db_host = '172.16.1.2'
db_port = 27017

current_year = date.today().year
current_month = date.today().month
current_day = date.today().day


def ensure_paths():
    from pathlib import Path
    Path(process_path).mkdir(parents=True, exist_ok=True)
    Path(processing_path).mkdir(parents=True, exist_ok=True)
    Path(processed_path).mkdir(parents=True, exist_ok=True)
    Path(result_path).mkdir(parents=True, exist_ok=True)
    Path(logs_path).mkdir(parents=True, exist_ok=True)
    Path(captcha_path).mkdir(parents=True, exist_ok=True)
    Path(pdf_path).mkdir(parents=True, exist_ok=True)
    Path(excel_path).mkdir(parents=True, exist_ok=True)
    Path(drivers_path).mkdir(parents=True, exist_ok=True)


ensure_paths()
