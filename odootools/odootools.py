# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.relativedelta import relativedelta

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
