#!/usr/bin/env python3

import os, sys
import logging
import argparse

from assets.lib.commons import *

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

    parser.add_argument("-d", "--debug",
                        help="provide debug information",
                        action="store_true")


    subparsers = parser.add_subparsers(dest="command", help="Commands")
    parser_c = subparsers.add_parser("compile",
                                     help="compile the datalog program")

    parser_r = subparsers.add_parser("run",
                                     help="run the datalog program")
    parser_r.add_argument("-f", "--force", action="store_true",
                          help="forces to use the interpreter even if a binary exists")
    parser_r.add_argument("-d", "--dest", action="store",
                          default=None,
                          type=str,
                          help="a filename where to store the results")
    parser_r.add_argument("source",
                          help="a list of any number of source files",
                          nargs="+")

    parser_t = subparsers.add_parser("test",
                                     help="test the datalog program, do not provide additional"
                                          " options before. Regular unittest options can be added")

    properties["args"], unknown = parser.parse_known_args()



def setup_logger():
    """Set up the logger."""
    logger = logging.getLogger("pass_project")
    logger.setLevel(logging.DEBUG)
    console = logging.StreamHandler()
    logfile = logging.FileHandler(os.path.join(properties["LOG_DIR"], "taint_analysis.yaml"), 'a')
    console_formatter = logging.Formatter("%(message)s")
    logfile_formatter = logging.Formatter("---\ntime: %(asctime)s\ntrace: %(name)s\n"
                                          "level: %(levelname)s\nmessage:\n  \"%(message)s\"")

    console.setFormatter(console_formatter)
    logfile.setFormatter(logfile_formatter)

    if properties["args"].debug:
        logfile.setLevel(logging.DEBUG)
    else:
        logfile.setLevel(logging.WARNING)

    if properties["args"].verbose:
        console.setLevel(logging.INFO)
    elif not properties["args"].quiet:
        console.setLevel(logging.WARNING)
    else:
        console.setLevel(logging.ERROR)

    logger.addHandler(console)
    logger.addHandler(logfile)
