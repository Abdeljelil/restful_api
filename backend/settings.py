import os

from tornado.log import enable_pretty_logging, logging

LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)
enable_pretty_logging()

os.environ['PYTHONASYNCIODEBUG'] = '1'

MONGO_DB_NAME = "test_db"
MONGO_KW = dict(
    host='mongodb://127.0.0.1/test_db')
