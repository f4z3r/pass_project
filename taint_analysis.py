#!/usr/bin/env python3

if __name__ == "__main__":
    import os, sys
    import subprocess
    from datetime import datetime

    from assets.lib import utils
    from assets.lib.parser import Parser
    from assets.lib.commons import *

    utils.setup_parser()
    utils.setup_logger()
    logger = utils.get_logger("taint_analysis")

    if properties["args"].command == "run":
        for source in properties["args"].source:
            filename = ""
            parser = Parser(source)
            parser.parse()
            logger.info("Launching an analysis ...")
            try:
                process = subprocess.run(["souffle",
                                          "--output-dir=" + properties["OUTPUT_DIR"],
                                          "--fact-dir=" + properties["FACTS_DIR"],
                                          properties["DL_FILE"],
                                         ],
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         check=True)
                logger.info("Analysis finished with code: {}".format(process.returncode))

                if process.returncode == 0:
                    filename = os.path.join(properties["OUTPUT_DIR"],
                                            "{}.csv".format(datetime.now()))
                    os.rename(os.path.join(properties["OUTPUT_DIR"], "res.csv"), filename)

                else:
                    logger.error("Something unexpected happened during analysis, please try again.")
                    continue

            except subprocess.CalledProcessError as err:
                logger.error("Could not perform: {}\n{}".format(err.cmd, err))
                logger.info("{}".format(err.stderr.decode("ascii")))
                continue

            # work with file


    if properties["args"].command == "compile":
        logger.info("Launching compiler")
        try:
            process = subprocess.run(["souffle",
                                      "--dl-program=" + os.path.join(properties["BIN_DIR"],
                                                                     "taint_analyser"),
                                      "--jobs=2",
                                      properties["DL_FILE"],
                                     ],
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     check=True)
            logger.info("Compiler finished with code: {}".format(process.returncode))

        except subprocess.CalledProcessError as err:
            logger.error("An error occured:\n  {}".format(err))
            logger.info("Error returned:\n  {}".format(err.stderr.decode("ascii")))


