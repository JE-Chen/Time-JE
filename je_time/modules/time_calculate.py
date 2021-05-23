import datetime
import time


def get_time_now():
    return time.strftime("%c")


def get_now_time_local():
    return time.strftime("%x")


def get_year():
    return time.strftime("%Y")


def get_month():
    return time.strftime("%m")


def get_day():
    return time.strftime("%d")


def get_hour():
    return time.strftime("%H")


def get_minute():
    return time.strftime("%M")


def get_sec():
    return time.strftime("%S")


def get_day_before(before_days):
    now_data_time = datetime.datetime.now()
    before_days = datetime.timedelta(days=before_days)
    time_data = now_data_time - before_days
    return time_data


def get_hour_before(before_hours):
    now_data_time = datetime.datetime.now()
    before_days = datetime.timedelta(hours=before_hours)
    time_data = now_data_time - before_days
    return time_data


def get_minute_before(before_minutes):
    now_data_time = datetime.datetime.now()
    before_days = datetime.timedelta(minutes=before_minutes)
    time_data = now_data_time - before_days
    return time_data


def get_second_before(before_seconds):
    now_data_time = datetime.datetime.now()
    before_days = datetime.timedelta(seconds=before_seconds)
    time_data = now_data_time - before_days
    return time_data


def get_day_after(after_days):
    now_data_time = datetime.datetime.now()
    before_days = datetime.timedelta(days=after_days)
    time_data = now_data_time + before_days
    return time_data


def get_hour_after(after_hours):
    now_data_time = datetime.datetime.now()
    before_days = datetime.timedelta(hours=after_hours)
    time_data = now_data_time + before_days
    return time_data


def get_minute_after(after_minutes):
    now_data_time = datetime.datetime.now()
    before_days = datetime.timedelta(minutes=after_minutes)
    time_data = now_data_time + before_days
    return time_data


def get_second_after(after_seconds):
    now_data_time = datetime.datetime.now()
    before_days = datetime.timedelta(seconds=after_seconds)
    time_data = now_data_time + before_days
    return time_data
