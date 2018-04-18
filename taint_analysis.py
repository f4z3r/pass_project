#!/usr/bin/env python3

if __name__ == "__main__":
    import os, sys
    import subprocess

    from assets.lib import utils
    from assets.lib.commons import *
    from assets.lib import analysis

    utils.setup_parser()
    utils.setup_logger()
    logger = utils.get_logger("taint_analysis")

    if properties["args"].command == "run":
        for source in properties["args"].source:
            analysis.Analysis(source).run()



    if properties["args"].command == "compile":
        logger.info("Launching compiler")
        try:
            process = subprocess.run(["souffle",
                                      "--dl-program=" + os.path.join(properties["BIN_DIR"],
                                                                     "taint_analyser"),
                                      "--jobs=2",
                                      "--output-dir=" + properties["OUTPUT_DIR"],
                                      "--fact-dir=" + properties["FACTS_DIR"],
                                      properties["DL_FILE"],
                                     ],
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     check=True)
            logger.info("Compiler finished with code: {}".format(process.returncode))

        except subprocess.CalledProcessError as err:
            logger.error("An error occured:\n  {}".format(err))
            logger.info("Error returned:\n  {}".format(err.stderr.decode("ascii")))

    if properties["args"].command == "test":
        import unittest
        sys.argv[1:] = sys.argv[2:]
        unittest.main(module="assets.lib.tests")
