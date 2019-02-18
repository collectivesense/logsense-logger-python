#!/usr/bin/env python
import requests
import random
import time

if __name__ == "__main__":
    tries = 1000
    delay = 1

    for i in range(tries):
        if random.randint(0, 3) == 2:
            requests.get('http://localhost:5000/')

        if random.randint(0, 50) == 2:
            # This will trigger an exception every now and then
            requests.get('http://localhost:5000/foo/-1')

        requests.get('http://localhost:5000/foo/{}'.format(random.randint(0, 1000)))
        time.sleep(delay)
