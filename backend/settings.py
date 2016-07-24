from tornado.log import logging, enable_pretty_logging
import os

LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)
enable_pretty_logging()

os.environ['PYTHONASYNCIODEBUG'] = '1'

MONGO_DB_NAME = "streaming_master_db"
MONGO_KW = dict(
    host='mongodb://stream:stream159@178.18.31.138/streaming_master_db')
