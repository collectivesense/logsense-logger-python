# logsense-logger-python

Provides a set of wrapper classes and method for working
with Python and [LogSense](https://logsense.com)

# Usage

## Installation

```
pip3 install logsense-logger
```


## Wrapping logging

```
from logsense.handler import LogSenseHandler
from os import getenv
import logging

logsense_token = getenv('LOGSENSE_TOKEN', None)
log = logging.getLogger()
log.addHandler(LogSenseHandler(logsense_token))
log.setLevel(logging.INFO)


class Example:
    def __init__(self):
        self.bar = 42

    def foo(self):
        logging.info("Answer: {}".format(self.bar))


if __name__ == "__main__":
    ex = Example()
    ex.foo()
```

Now, just run the app, e.g.

```
LOGSENSE_TOKEN="63da4903-01e9-d1a4-82a8-9cf8cd63b7b5" python sample_logging.py
```

And your logs should flow to LogSense

## Metrics

The package also includes a simple example on how to measure method duration
and have ability to track metrics. All that needs to be done is providing
`LOGSENSE_TOKEN` environment variable and than annotating
methods that are to be measure with `@measure_duration()`. For example:

```
from logsense.metrics import measure_duration, setup_metrics
from os import getenv

logsense_token = getenv('LOGSENSE_TOKEN')
setup_metrics('myapp', logsense_token)


class MyComplexProcess:
    def __init__(self, how_many_times):
        self._how_many_times = how_many_times

    @measure_duration(extracted_params=['a'])
    def foo(self, a):
        x = 0
        for i in range(a*self._how_many_times):
            x = x+1
        return x
```

## Examples

Check the [example](example/) for actual usage examples