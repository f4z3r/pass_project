#!/usr/bin/env python3

if __name__ == "__main__":
    import os, sys

    from assets.lib import utils
    from assets.lib.parser import Parser
    from assets.lib.commons import *

    utils.setup_parser()
    utils.setup_logger()
    logger = utils.get_logger("taint_analysis")

    if properties["args"].command == "run":
        for source in properties["args"].source:
            parser = Parser(source)
            parser.parse()
            # Run the taint_analysis

    if properties["args"].command == "compile":
        # Compile the .dl file.
        pass


