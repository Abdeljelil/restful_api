import aiomotorengine

from backend import settings
from backend.views.user import UserView
from backend.views.user_group import UserGroupView

from tornado.options import define, options
from tornado.platform.asyncio import AsyncIOMainLoop
import tornado.web


define("port", default="8888", help="Server port")
define("bind", default="127.0.0.1", help="Bind ip address")


entry_points = [
    (r"/user_group(.*)", UserGroupView),
    (r"/user(.*)", UserView),

]


def main():

    print("in main with port {}".format(options.port))

    tonado_ioloop = AsyncIOMainLoop()

    tonado_ioloop.install()

    # creation tornado app should be after /
    # create ioloop install
    app = tornado.web.Application(
        entry_points,
        debug=True,
        # autoreload=True,
        # serve_traceback=True
    )

    aiomotorengine.connect(
        settings.MONGO_DB_NAME,
        io_loop=tonado_ioloop.asyncio_loop,
        **settings.MONGO_KW
    )

    settings.LOG.info(
        "Tornado server has been started on port {}".format(options.port)
    )
    app.listen(options.port, address=options.bind)
    tonado_ioloop.start()


if __name__ == '__main__':

    main()
