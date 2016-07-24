import asyncio
from aiomotorengine import connect
from tornado.platform.asyncio import AsyncIOMainLoop
import tornado.web
from backend.views.channel import ChannelView
from backend import settings


entry_points = [
    (r"/channel(.*)", ChannelView),
]


def main(port=8888):
    """
    main function of the server 
    only one parameter is required 
    port : port number of the service
    """
    AsyncIOMainLoop().install()
    ioloop = asyncio.get_event_loop()
    # creation of tornado app should be after /
    # the create of ioloop of asyncio
    app = tornado.web.Application(entry_points,
                                  debug=True,
                                  autoreload=True,
                                  serve_traceback=True)

    mongo_db = connect(settings.MONGO_DB_NAME,
                       io_loop=ioloop, **settings.MONGO_KW)

    settings.LOG.info(
        "Tornado server has been started on port {}".format(port))
    app.listen(port)
    try:
        ioloop.run_forever()
    except KeyboardInterrupt:
        settings.LOG.error("keyboard interrupt exception has been performed")
        mongo_db.connection.close()
        ioloop.run_until_complete()
        ioloop.close()
        settings.LOG.info("Tornado server stopped")

if __name__ == '__main__':

    main(8888)
