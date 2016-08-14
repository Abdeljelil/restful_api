import asyncio
import logging
import threading
import time
import unittest
from urllib.parse import urljoin

import requests

from backend import settings
from backend.server import main

TEST_API_PORT = 9900
REQUEST_TIME_OUT = 5

logging.basicConfig(level=logging.CRITICAL)

settings.LOG.setLevel(logging.CRITICAL)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.start_server()

    @classmethod
    def tearDownClass(cls):
        cls.stop_server()

    @classmethod
    def start_server(cls):

        cls.ioloop = asyncio.new_event_loop()
        cls.thread = threading.Thread(
            target=main,
            args=(TEST_API_PORT, cls.ioloop, )
        )

        cls.thread.start()

        # make sure that the server is stated
        time.sleep(0.5)

    @classmethod
    def stop_server(cls):

        cls.ioloop.stop()

    def make_url(self, route):

        base = "http://localhost:{}".format(TEST_API_PORT)

        return urljoin(base, route, allow_fragments=True)

    def send_request(self, *args, **kwargs):

        if "timeout" in kwargs:
            kwargs["timeout"] = REQUEST_TIME_OUT
        resonpse = requests.request(*args, **kwargs)
        return resonpse.json(), resonpse.status_code


class BaseFakeModel(object):

    metaclass = None

    fakedatadict = {}
