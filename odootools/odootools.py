# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar

def dt_range(start, stop=False, exclude_weekdays=[], exclude_dates=[]):
    exclude_dates = not isinstance(exclude_dates, (list, tuple)) and \
                    [exclude_dates] or exclude_dates
    exclude_dates = [isinstance(date, basestring) and datetime.strptime(date,
                    "%Y-%m-%d") or date for date in exclude_dates]
    if isinstance(start, basestring):
        start = datetime.strptime(start, "%Y-%m-%d")
    if stop and isinstance(stop, basestring):
        stop = datetime.strptime(stop, "%Y-%m-%d")
    while not stop or start <= stop:
        if start.weekday() not in exclude_weekdays:
            if start not in exclude_dates:
                yield start.strftime("%Y-%m-%d")
        start = start + relativedelta(days=1)

def last_day(date):
    if isinstance(date, basestring):
        date = datetime.strptime(date, "%Y-%m-%d")
    day = calendar.monthrange(date.year, date.month)[1]
    date = date + relativedelta(day=day)
    return date.strftime("%Y-%m-%d")

def first_day(date):
    if isinstance(date, basestring):
        date = datetime.strptime(date, "%Y-%m-%d")
    date = date + relativedelta(day=1)
    return date.strftime("%Y-%m-%d")

def interval_tuple(date):
    return first_day(date), last_day(date)

def next_day(date):
    if isinstance(date, basestring):
        date = datetime.strptime(date, "%Y-%m-%d")
    date = date + relativedelta(days=1)
    return date.strftime("%Y-%m-%d")

def next_month(date):
    if isinstance(date, basestring):
        date = datetime.strptime(date, "%Y-%m-%d")
    date = date + relativedelta(months=1)
    return date.strftime("%Y-%m-%d")

def next_month_last_day(date):
    if isinstance(date, basestring):
        date = datetime.strptime(date, "%Y-%m-%d")
    date = date + relativedelta(months=1)
    return last_day(date.strftime("%Y-%m-%d"))

def next_year(date):
    if isinstance(date, basestring):
        date = datetime.strptime(date, "%Y-%m-%d")
    date = date + relativedelta(years=1)
    return date.strftime("%Y-%m-%d")
