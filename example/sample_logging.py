#!/usr/bin/env python

from logsense.handler import LogSenseHandler, LogSenseRecordFormatter
from os import getenv
import logging

_logsense_token = getenv('LOGSENSE_TOKEN', None)

_handler = LogSenseHandler(_logsense_token)
_handler.setLevel(logging.INFO)
logging.getLogger().addHandler(_handler)

_console = logging.StreamHandler()
_console.setLevel(logging.DEBUG)
_console.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))
logging.getLogger().addHandler(_console)

logging.getLogger().setLevel(logging.INFO)


class Example:
    def __init__(self):
        self.bar = 42

    def foo(self):
        logging.info("Answer: %d", 42)


if __name__ == "__main__":
    ex = Example()
    ex.foo()
