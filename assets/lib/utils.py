#!/usr/bin/env python3

import os, sys
import logging
import argparse

from assets.lib.commons import *

logger = logging.getLogger(properties["package_name"] + "." + __name__)

def get_logger(name=None, root_name=properties["package_name"]):
    """Builds logger with correct name.
    Args:
        name (str): optional - name of the logger, usually __name__.
        root_name (str): optional - root name of the logger, usually the package name.
    Returns:
        logging.Logger: A logger.
    """
    if name:
        return logging.getLogger(root_name + "." + name)
    else:
        return logging.getLogger(root_name)

def setup_parser():
    """Sets up the command line argument parser."""
    parser = argparse.ArgumentParser(description="Control program to launch all actions related to"
                                                 " this project.")

    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument("-v", "--verbose",
                                 help="provide verbose output",
                                 action="store_true")
    verbosity_group.add_argument("-q", "--quiet",
                                 help="provide next to no output unless an error occured",
                                 action="store_true")

    subparsers = parser.add_subparsers(dest="command", help="Commands")
    parser_c = subparsers.add_parser("compile",
                                     help="compile the datalog program")

    parser_r = subparsers.add_parser("run",
                                     help="run the datalog program")
    parser_r.add_argument("-d", "--dest", action="store",
                          default=None,
                          type=str,
                          help="a filename where to store the results")
    parser_r.add_argument("source",
                          help="a list of any number of source files",
                          nargs="+")

    properties["args"] = parser.parse_args()



def setup_logger():
    """Set up the logger."""
    file_path = os.path.dirname(os.path.abspath(__file__))

    try:
        os.mkdir(os.path.join(file_path, "../logs"))
    except OSError:
        pass

    logger = logging.getLogger("pass_project")
    logger.setLevel(logging.DEBUG)
    console = logging.StreamHandler()
    logfile = logging.FileHandler(os.path.join(file_path, "../logs/taint_analysis.yaml"), 'a')
    console_formatter = logging.Formatter("%(message)s")
    logfile_formatter = logging.Formatter("---\ntime: %(asctime)s\ntrace: %(name)s\n"
                                          "level: %(levelname)s\nmessage:\n  %(message)s")

    console.setFormatter(console_formatter)
    logfile.setFormatter(logfile_formatter)

    logfile.setLevel(logging.WARNING)

    if not properties["args"].quiet:
        console.setLevel(logging.WARNING)
    elif properties["args"].verbose:
        console.setLevel(logging.INFO)
    else:
        console.setLevel(logging.ERROR)

    logger.addHandler(console)
    logger.addHandler(logfile)
