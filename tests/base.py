import logging
import json

import tornado.web
from backend import settings
from backend.server import entry_points
from tornado.testing import AsyncHTTPTestCase

import aiomotorengine
REQUEST_TIME_OUT = 5

logging.basicConfig(level=logging.CRITICAL)

# settings.LOG.setLevel(logging.CRITICAL)


class BaseTestCase(AsyncHTTPTestCase):

    def get_new_ioloop(self):

        io_loop = tornado.platform.asyncio.AsyncIOMainLoop()

        return io_loop

    def setUp(self):

        super(BaseTestCase, self).setUp()

        aiomotorengine.connect(
            settings.MONGO_DB_NAME,
            io_loop=self.io_loop.asyncio_loop,
            **settings.MONGO_KW
        )

    def get_app(self):

        app = tornado.web.Application(
            entry_points,

        )

        return app

    def make_url(self, url):
        return url

    def send_request(self, *args, **kwargs):

        response = self.fetch(
            args[1],
            method=args[0],
            body=kwargs.get("data", None),
            follow_redirects=False,
            request_timeout=REQUEST_TIME_OUT
        )

        decode_response = response.body.decode("utf-8")
        json_response = json.loads(decode_response)
        return json_response, response.code
