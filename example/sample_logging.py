from logsense.handler import LogSenseHandler, LogSenseRecordFormatter
from os import getenv
import logging

_customer_token = getenv('LOGSENSE_CUSTOMER_TOKEN', None)

_custom_format = {
    'host': '%(hostname)s',
    'where': '%(module)s.%(funcName)s',
    'type': '%(levelname)s',
    'stack_trace': '%(exc_text)s'
}
_formatter = LogSenseRecordFormatter(_custom_format)
_handler = LogSenseHandler(_customer_token)
_handler.setFormatter(_formatter)
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
        logging.info("Answer: {}".format(self.bar))


if __name__ == "__main__":
    ex = Example()
    ex.foo()
