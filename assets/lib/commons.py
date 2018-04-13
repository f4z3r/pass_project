#!/usr/bin/env python3

"""All common features."""

import os, sys

properties = {
    "args": None,
    "package_name": "pass_project",
    "ROOT_DIR": os.path.dirname(sys.modules["__main__"].__file__),
    "FACTS_DIR": os.path.join(os.path.dirname(sys.modules["__main__"].__file__), "assets/datalog"),
}
