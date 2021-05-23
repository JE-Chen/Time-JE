import calendar
import time


def get_year_calendar():
    return calendar.calendar(int(time.strftime("%Y")))


def get_month_calendar():
    return calendar.month(int(time.strftime("%Y")), int(time.strftime("%m")))


def get_is_leap(year):
    return calendar.isleap(year)


def get_leap_days(year, year2):
    return calendar.leapdays(year, year2)

