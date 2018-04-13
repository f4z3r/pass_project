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

    parts = parser.add_mutually_exclusive_group()
    parts.add_argument("-p", "--parse",
                       help="only parse the source code without analysing it",
                       action="store_true")
    parts.add_argument("-a", "--analyse",
                       help="skip parsing and only perform analysis. This can only be performed if"
                       " parsed data exists",
                       action="store_true")

    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument("-v", "--verbose",
                                 help="provide verbose output",
                                 action="store_true")
    verbosity_group.add_argument("-q", "--quiet",
                                 help="provide next to no output unless an error occured",
                                 action="store_true")

    parser.add_argument("-d", "--dest", action="store",
                        default=None,
                        type=str,
                        help="a filename where to store the results")

    parser.add_argument("source",
                        help="a list of any number of source files",
                        nargs="*")

    args, unknown = parser.parse_known_args()

    return args

if __name__ == "__main__":
    file_path = os.path.dirname(os.path.abspath(__file__))

    args = setup_parser()

    # Setup a logger to output the solution to destination (file, console).

    if args.parse:
        # Parse
        pass
    elif args.analyse:
        # Analyse
        pass
    else:
        # Do all
        pass
