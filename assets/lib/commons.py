#!/usr/bin/env python3

"""All common features."""

import os, sys

properties = {
    "args": None,
    "package_name": "pass_project",
    "ROOT_DIR": os.path.dirname(sys.modules["__main__"].__file__),
    "FACTS_DIR": os.path.join(os.path.dirname(sys.modules["__main__"].__file__), "assets/datalog"),
    "OUTPUT_DIR": os.path.join(os.path.dirname(sys.modules["__main__"].__file__), "assets/output"),
    "LOG_DIR": os.path.join(os.path.dirname(sys.modules["__main__"].__file__), "assets/logs"),
    "BIN_DIR": os.path.join(os.path.dirname(sys.modules["__main__"].__file__), "assets/bin"),
    "DL_FILE": os.path.join(os.path.dirname(sys.modules["__main__"].__file__),
                            "assets/datalog/taint_analyser.dl"),
}


try:
    os.mkdir(properties["OUTPUT_DIR"])
except OSError:
    pass

try:
    os.mkdir(properties["LOG_DIR"])
except OSError:
    pass

try:
    os.mkdir(properties["BIN_DIR"])
except OSError:
    pass
