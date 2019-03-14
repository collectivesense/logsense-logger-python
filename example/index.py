from logsense.metrics import measure_duration, setup_metrics
from logsense.handler import LogSenseHandler, LogSenseRecordFormatter

from flask import Flask
import logging

# Fetch token
from os import getenv
logsense_token = getenv('LOGSENSE_TOKEN')

# Setup metrics
setup_metrics('index.py', logsense_token)

# Setup logging
_handler = LogSenseHandler(logsense_token)
_handler.setLevel(logging.INFO)
logging.getLogger().addHandler(_handler)

app = Flask(__name__)


class SomeComplexProcess:
    def __init__(self, how_many_times):
        self._how_many_times = how_many_times

    @measure_duration(extracted_params=['a'])
    def foo(self, a):
        if a < 0:
            raise RuntimeError("Negative numbers are not accepted")

        x = 0
        for i in range(a*self._how_many_times):
            x = x+1
        return x


example = SomeComplexProcess(10000)


@app.route("/")
@measure_duration()
def hello():
    app.logger.info("Hello")
    return "Hello World!"


@app.route("/foo/<a>")
def test_complex_process(a):
    app.logger.info("A complex process was called with param: %s", a)
    return "Result: {}".format(example.foo(int(a)))
