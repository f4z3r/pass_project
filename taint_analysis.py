#!/usr/bin/env python3

import os, sys
import argparse

def setup_parser():
    """Sets up the command line argument parser.

    Returns:
        argparse.Namespace: the command line arguments.
    """
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

    args = parser.parse_args()

    return args

if __name__ == "__main__":
    file_path = os.path.dirname(os.path.abspath(__file__))

    args = setup_parser()

    # Setup a logger to output the solution to destination (file, console).

