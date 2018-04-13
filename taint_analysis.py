#!/usr/bin/env python3

if __name__ == "__main__":
    import os, sys

    from assets.lib import utils
    from assets.lib.parser import Parser

    file_path = os.path.dirname(os.path.abspath(__file__))

    utils.setup_parser()
    utils.setup_logger()
    logger = utils.get_logger("taint_analysis")

    parser = Parser("somefile.source")

