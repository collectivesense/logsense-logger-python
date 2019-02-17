from flask import Flask
from logsense.metrics import measure_duration, setup_metrics
from os import getenv

customer_token = getenv('LOGSENSE_CUSTOMER_TOKEN')
setup_metrics(customer_token)

app = Flask(__name__)


class SomeComplexProcess:
    def __init__(self, how_many_times):
        self._how_many_times = how_many_times

    @measure_duration(extracted_params=['a'])
    def foo(self, a):
        x = 0
        for i in range(a*self._how_many_times):
            x = x+1
        return x


example = SomeComplexProcess(10000)


@app.route("/")
@measure_duration()
def hello():
    return "Hello World!"


@app.route("/foo/<a>")
def test_complex_process(a):
    return "Result: {}".format(example.foo(int(a)))
