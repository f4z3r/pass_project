#!/usr/bin/env python3

"""Module containing all tests."""

import os
import unittest
import csv

from assets.lib.commons import *
from assets.lib import utils
from assets.lib import analysis

class TestDatalog(unittest.TestCase):
    """Class testing all datalog functionalities."""

    def test_case_1(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "test_case_1.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "test_case_1.csv"))

    def test_case_2(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "test_case_2.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "test_case_2.csv"))

    def test_case_3(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "test_case_3.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "test_case_3.csv"))

    def test_case_4(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "test_case_4.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "test_case_4.csv"))

    def test_case_5(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "test_case_5.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "test_case_5.csv"))

    def test_case_6(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "test_case_6.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "test_case_6.csv"))

    def test_case_7(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "test_case_7.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "test_case_7.csv"))

    def test_case_8(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "test_case_8.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "test_case_8.csv"))

    def test_case_9(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "test_case_9.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "test_case_9.csv"))

    def test_verify_case_1(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_1.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_1.csv"))

    def test_verify_case_2(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_2.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_2.csv"))

    def test_verify_case_3(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_3.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_3.csv"))

    def test_verify_case_4(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_4.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_4.csv"))

    def test_verify_case_5(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_5.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_5.csv"))

    def test_verify_case_6(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_6.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_6.csv"))

    def test_verify_case_7(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_7.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_7.csv"))

    def test_verify_case_8(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_8.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_8.csv"))

    def test_verify_case_9(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_9.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_9.csv"))

    def test_verify_case_10(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_10.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_10.csv"))

    def test_verify_case_11(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_11.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_11.csv"))

    def test_verify_case_12(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_12.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_12.csv"))

    def test_verify_case_13(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_13.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_13.csv"))

    def test_verify_case_14(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_14.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_14.csv"))

    def test_verify_case_15(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_15.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_15.csv"))

    def test_verify_case_16(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_16.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_16.csv"))

    def test_verify_case_17(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_17.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_17.csv"))

    def test_verify_case_18(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_18.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_18.csv"))

    def test_verify_case_19(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_19.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_19.csv"))

    def test_verify_case_20(self):
        outputfile = analysis.Analysis(os.path.join(properties["TEST_DIR"], "verify_case_20.dl")).run()
        self._compare_files(outputfile, os.path.join(properties["TEST_DIR"], "verify_case_20.csv"))




    def _compare_files(self, filename_output, filename_gt):
        output = utils.read_csv(filename_output)
        result = utils.read_csv(filename_gt)

        # Check that the same variables are being sanitized
        res_var = [res[0] for res in result]
        out_var = [out[0] for out in output]
        self.assertEqual(res_var, out_var,
                         "Too many or too few sanitations. See file {}".format(filename_output))

        # Check if all results are present
        for res in result:
            for out in output:
                if res[0] == out[0]:
                    if int(res[1]) <= int(out[1]) <= int(res[2]):
                        break
            else:
                self.fail("{} is not in [{}, {}] for {}".format(out[1], res[1], res[2], out[0]) + \
                          "\nSee file {}".format(filename_output))





