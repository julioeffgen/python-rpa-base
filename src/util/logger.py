# from robot.api import logger
from src.util import date


# def print_to_console(message):
#     logger.console(f"{DateUtil.find_current_date()} - {message}")


def log(message):
    # logger.console(f"{DateUtil.find_current_date()} - {message}")
    print(f"{date.find_current_date()} - {message}")
