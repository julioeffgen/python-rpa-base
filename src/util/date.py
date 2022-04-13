from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import *


def string_to_date(value, date_format):
    return datetime.strptime(value, date_format)


def date_to_string(value, date_format):
    return value.strftime(date_format)


def add_day(value, days):
    if days < 0:
        return value - timedelta(days=(days * -1))
    return value + timedelta(days=days)


def add_month(value, months):
    if months < 0:
        return value - relativedelta(months=(months * -1))
    return value + relativedelta(months=months)


def add_year(value, years):
    if years < 0:
        return value - relativedelta(years=(years * -1))
    return value + relativedelta(years=years)


def day_of_week():
    return datetime.today().weekday()


def current_date_string(date_format):
    return datetime.today().strftime(date_format)


def previous_date_string(date_format):
    return add_day(datetime.today(), -1).strftime(date_format)


def split_date(ref_date, separator):
    return ref_date.split(separator)


def find_current_date():
    return datetime.today()


def first_day_of_month(current):
    return current.replace(day=1)


def first_day_of_year(date_format):
    first_day = find_current_date().replace(day=1)
    first_day = first_day.replace(month=1)
    return date_to_string(first_day, date_format)


def last_day_of_month(current):
    last_day = first_day_of_month(current)
    last_day = add_month(last_day, 1)
    last_day = add_day(last_day, -1)
    return last_day


def last_day_of_earlier_month(date_format, months_off):
    target_month = find_current_date()
    months_to_remove = int(months_off)
    if months_to_remove > 0:
        target_month = add_month(target_month, (months_to_remove - 1) * -1)
    last_day = first_day_of_month(target_month)
    last_day = add_day(last_day, -1)
    return date_to_string(last_day, date_format)


def remove_days(value, days):
    return value - timedelta(days=days)
