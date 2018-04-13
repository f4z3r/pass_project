#!/usr/bin/env python3

"""Module containing a parser."""

import os

from assets.lib.commons import *
from assets.lib import utils

logger = utils.get_logger(__name__)

class Parser:
    """A parser for the source code provided to the taint_analyser."""

    def __init__(self, filename):
        """Initialise the parser.

        Args:
            filename (str): the filename of the source code.
        """
        logger.info("Initialising parser for source {}".format(filename))
        self.filename = os.path.join(filename, properties["ROOT_DIR"])

