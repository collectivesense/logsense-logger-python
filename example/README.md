# Sample applications using Logsense logging

## Flask web server with metrics and logging

To run:

```
pip install Flask
LOGSENSE_TOKEN=<your token> FLASK_APP=index.py flask run
```

To test it, execute `./benchmark.py`

## Simple app with logging

Run `LOGSENSE_TOKEN=<your token> ./sample_logging.py` to generate a log
