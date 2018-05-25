#!/usr/bin/env python3

"""Module containing a parser."""

import os
import re

from assets.lib.commons import *
from assets.lib import utils

logger = utils.get_logger(__name__)

class Parser:
    """A parser for the source code provided to the taint_analyser."""

    def __init__(self, filename):
        """Initialise the parser.

        Args:
            filename (str): the filename of the source code.
        """
        self.filename = os.path.join(properties["ROOT_DIR"], filename)
        self.text = ""
        logger.info("Initialising parser for source {}".format(self.filename))

        self.source_facts = os.path.join(properties["FACTS_DIR"], "source.facts")
        self.sink_facts = os.path.join(properties["FACTS_DIR"], "sink.facts")
        self.follows_facts = os.path.join(properties["FACTS_DIR"], "follows.facts")
        self.if_stat_facts = os.path.join(properties["FACTS_DIR"], "if.facts")
        self.join_facts = os.path.join(properties["FACTS_DIR"], "join.facts")
        self.assign_facts = os.path.join(properties["FACTS_DIR"], "assign.facts")

        self._source_file = None
        self._sink_file = None
        self._follows_file = None
        self._if_stat_file = None
        self._join_file = None
        self._assign_file = None

        self.token = re.compile(r"\s*(?P<token>\w+\s*\([\s,\w<>=\"]+\))\s*")
        self.source = re.compile(r"source\s*\(\s*\"?[lL]?(?P<label>\w+)\"?\s*,\s*\"?"
                                 r"(?P<var>\w+)\"?\s*\)")
        self.sink = re.compile(r"sink\s*\(\s*\"?[lL]?(?P<label>\w+)\"?\s*,"
                               r"\s*\"?(?P<var>\w+)\"?\s*\)")
        self.follows = re.compile(r"follows\s*\(\s*\"?[lL]?(?P<after>\w+)\"?\s*,"
                                  r"\s*\"?[lL]?(?P<before>\w+)\"?\s*\)")
        self.if_stat = re.compile(r"if\s*\(\s*\"?[lL]?(?P<label>\w+)\"?\s*,\s*\"?[lL]?(?P<jump>\w+)"
                                  r"\"?\s*,\s*-?\s*\"?-?(?P<variable1>\w+)\"?\s*,"
                                  r"\s*\"?-?(?P<variable2>\w+)\"?\s*\)")
        self.join = re.compile(r"join\s*\(\s*\"?[lL]?(?P<label>\w+)\"?\s*,\s*\"?[lL]?(?P<join1>\w+)"
                               r"\"?\s*,\s*\"?[lL]?(?P<join2>\w+)\"?\s*\)")
        self.assign = re.compile(r"assign\s*\(\s*\"?[lL]?(?P<label>\w+)\"?\s*,"
                                 r"\s*\"?(?P<receiver>\w+)\"?\s*,\s*\"?(?P<item1>\w+)\"?\s*,"
                                 r"\s*\"?(?P<item2>\w+)\"?\s*\)")


    def parse(self):
        """Parses the source code. Note this does not check for correctness. Hence incorrect
        source code can produce undefined behaviour.
        """
        logger.info("Started parsing file: {}".format(self.filename))

        with open(self.filename, 'r') as file:
            self.text = file.read()

        self._source_file = open(self.source_facts, 'w')
        self._sink_file = open(self.sink_facts, 'w')
        self._follows_file = open(self.follows_facts, 'w')
        self._if_stat_file = open(self.if_stat_facts, 'w')
        self._join_file = open(self.join_facts, 'w')
        self._assign_file = open(self.assign_facts, 'w')

        token = self._parse_token()

        while token is not None:
            if re.fullmatch(self.source, token) is not None:
                match = re.fullmatch(self.source, token)
                logger.debug("source: {}".format(token))
                self._source_file.write("{}\t{}\n".format(match.group("label"), match.group("var")))
            elif re.fullmatch(self.sink, token) is not None:
                match = re.fullmatch(self.sink, token)
                logger.debug("sink: {}".format(token))
                self._sink_file.write("{}\t{}\n".format(match.group("label"), match.group("var")))
            elif re.fullmatch(self.follows, token) is not None:
                match = re.fullmatch(self.follows, token)
                logger.debug("follows: {}".format(token))
                self._follows_file.write("{}\t{}\n".format(match.group("after"),
                                                           match.group("before")))
            elif re.fullmatch(self.if_stat, token) is not None:
                match = re.fullmatch(self.if_stat, token)
                logger.debug("if_stat: {}".format(token))
                self._if_stat_file.write("{}\t{}\t{}\t{}\n".format(match.group("label"),
                                                                   match.group("jump"),
                                                                   match.group("variable1"),
                                                                   match.group("variable2")))
            elif re.fullmatch(self.join, token) is not None:
                match = re.fullmatch(self.join, token)
                logger.debug("join: {}".format(token))
                self._join_file.write("{}\t{}\t{}\n".format(match.group("label"),
                                                            match.group("join1"),
                                                            match.group("join2")))
            elif re.fullmatch(self.assign, token) is not None:
                match = re.fullmatch(self.assign, token)
                logger.debug("assign: {}".format(token))
                self._assign_file.write("{}\t{}\t{}\t{}\n".format(match.group("label"),
                                                                  match.group("receiver"),
                                                                  match.group("item1"),
                                                                  match.group("item2")))
            else:
                logger.warning("unknown: {}".format(token))

            token = self._parse_token()

        logger.info("Finished parsing file: {}".format(self.filename))


        self._source_file.close()
        self._sink_file.close()
        self._follows_file.close()
        self._if_stat_file.close()
        self._join_file.close()
        self._assign_file.close()


    def _parse_token(self):
        """Parse a single token of the input.

        Returns:
            str: the string matched by the token.
        """
        match = re.search(self.token, self.text)
        if match is not None:
            end = match.end()
            self.text = self.text[end:]

            logger.debug("'{}' matched a token.".format(match.group("token")))
            return match.group("token")

        logger.debug("No token match found.")
        return None





