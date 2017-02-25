#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_odootools
----------------------------------

Tests for `odootools` module.
"""


import sys
import unittest

from odootools import odootools


class TestOdootools(unittest.TestCase):

    def setUp(self):
        self.start = '2017-02-27'
        self.stop = '2017-03-02'

    def test_dt_range(self):
        dr = odootools.DateRange(self.start, self.stop)
        dates = [x for x in dr]
        results = [
            '2017-02-27',
            '2017-02-28',
            '2017-03-01',
            '2017-03-02',
        ]
        self.assertEqual(dates, results, "DateRange return error, waiting {} and getting {}".format(
            results, dates
        ))

    def test_date_next_day(self):
        date = odootools.Date(self.start).next_day().value
        result = '2017-02-28'
        self.assertEqual(date, result, "Date next day return error, waiting {} and getting {}".format(
            result, date
        ))

    def test_date_prev_day(self):
        date = odootools.Date(self.start).prev_day().value
        result = '2017-02-26'
        self.assertEqual(date, result, "Date previous day return error, waiting {} and getting {}".format(
            result, date
        ))

    def test_date_next_month(self):
        date = odootools.Date(self.start).next_month().value
        result = '2017-03-27'
        self.assertEqual(date, result, "Date next month return error, waiting {} and getting {}".format(
            result, date
        ))

    def test_date_next_year(self):
        date = odootools.Date(self.start).next_year().value
        result = '2018-02-27'
        self.assertEqual(date, result, "Date next year return error, waiting {} and getting {}".format(
            result, date
        ))
