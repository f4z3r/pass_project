#!/usr/bin/env python3

"""Module containing all tests."""

import os
import unittest

from assets.lib.commons import *
from assets.lib import utils

logger = utils.get_logger(__name__)

class TestDatalog(unittest.TestCase):
    """Class testing all datalog functionalities."""

    def test_case_1(self):
        self.assertEqual(0, 0)
