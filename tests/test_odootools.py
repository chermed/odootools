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

    def test_dt_range(self):
        start = '2017-02-27'
        stop = '2017-03-02'
        dates = [x for x in odootools.dt_range(start, stop)]
        results = [
            '2017-02-27',
            '2017-02-28',
            '2017-03-01',
            '2017-03-02',
        ]
        self.assertEqual(dates, results, "dt_range return error")
