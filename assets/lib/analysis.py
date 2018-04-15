#!/usr/bin/env python3

"""Module containing an analysis class."""

import os, sys
import subprocess
from datetime import datetime

from assets.lib import utils
from assets.lib.commons import *
from assets.lib.parser import Parser


logger = utils.get_logger(__name__)

class Analysis:
    """A class performing an analysis using the Datalog program."""

    def __init__(self, filename):
        """Initialise the analysis.

        Args:
            filename (str): The filename of the source code on which to perform the analysis.
        """
        self.filename = filename
        self.output_file = None
        self.use_bin = False

        # check if compiled code exists
        if properties["args"].force:
            logger.info("Using interpreter.")
        elif "taint_analyser" in os.listdir(properties["BIN_DIR"]):
            self.use_bin = True
            logger.info("Binary found.")
        else:
            logger.warning("No binary found, using interpreter.")

        self.parser = Parser(self.filename)

    def run(self):
        """Run the anlysis."""
        logger.info("Launching parser ...")
        self.parser.parse()

        logger.info("Launching the analysis ...")
        try:
            process = None
            if self.use_bin:
                process = subprocess.run([os.path.join(properties["BIN_DIR"], "taint_analyser")],
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         check=True)
                logger.info("Analysis finished with code: {}".format(process.returncode))
            else:
                process = subprocess.run(["souffle",
                                          "--output-dir=" + properties["OUTPUT_DIR"],
                                          "--fact-dir=" + properties["FACTS_DIR"],
                                          properties["DL_FILE"],
                                         ],
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         check=True)
                logger.info("Analysis finished with code: {}".format(process.returncode))

            if process is not None and process.returncode == 0:
                self.output_file = os.path.join(properties["OUTPUT_DIR"],
                                                "{}.csv".format(datetime.now()))
                os.rename(os.path.join(properties["OUTPUT_DIR"], "res.csv"), self.output_file)
            else:
                logger.error("Something unexpected happened during analysis, please try again.")
                return

        except subprocess.CalledProcessError as err:
            logger.error("An error occured:\n  {}".format(err))
            logger.info("Error returned:\n  {}".format(err.stderr.decode("ascii")))
            return


        # Work with file
