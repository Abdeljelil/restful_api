import asyncio

import tornado.web
from aiomotorengine import connect
from tornado.platform.asyncio import AsyncIOMainLoop

from backend import settings
from backend.views.channel import ChannelView

entry_points = [
    (r"/channel(.*)", ChannelView),
]


def main(port=8888, ioloop=None):
    """
    main function of the server
    only one parameter is required
    port : port number of the service
    """
    print("in main with port {}".format(port))

    # start event loop required if we'll run serve /
    # in thread like the example in unittest
    if ioloop is None:
        ioloop = asyncio.new_event_loop()

    asyncio.set_event_loop(ioloop)

    AsyncIOMainLoop().install()

    # creation of tornado app should be after /
    # the create of ioloop of asyncio
    app = tornado.web.Application(entry_points,
                                  debug=True,
                                  autoreload=True,
                                  serve_traceback=True)

    connect(settings.MONGO_DB_NAME,
            io_loop=ioloop, **settings.MONGO_KW)

    settings.LOG.info(
        "Tornado server has been started on port {}".format(port))
    app.listen(port)

    ioloop.run_forever()


if __name__ == '__main__':

    main(8888)
