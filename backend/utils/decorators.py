import sys
import traceback

from tornado import gen
from tornado.escape import json_encode

from backend.settings import LOG
from backend.utils.exceptions import UnknownError


def view_wrapper(func):
    @gen.coroutine
    def r_view_wrapper(self, *args, **kwargs):

        response = None
        status = 200
        try:
            response = yield func(self, *args, **kwargs)
        except Exception as e:
            response, status = debug(e, func, args, kwargs)

        self.clear()
        self.set_status(status)
        self.set_header("Content-Type", "application/json")
        if response is None:
            self.write(json_encode({}))
        else:
            self.write(json_encode(response))

        self.finish()

    return r_view_wrapper


def debug(exception, method, args, kwargs):
    '''
    Return a Json response if an error has been raised
    '''
    type_, value, traceback_ = sys.exc_info()

    if hasattr(exception, 'traceback') is False:

        exception = UnknownError(message=str(exception))

    exception.traceback = traceback.format_tb(traceback_)
    exception.type_ = str(type_)
    exception.value = str(value)

    error = dict(
        exception=exception.name,
        type=exception.type_,
        value=exception.value,
        traceback=exception.traceback,
        method=method.__name__,
        kwargs=str(kwargs),
        args=str(args),
        body=exception.body
    )

    # PRINT ERROR IN THE LOG FILE
    LOG.error("*" * 30 + " ERROR " + "*" * 30)
    LOG.error("Exception : " + str(exception.name))
    LOG.error("Type : " + str(exception.type_))
    LOG.error("Value : " + str(exception.value))
    LOG.error("Method : " + str(method.__name__))
    LOG.error("kwargs : " + str(kwargs))
    LOG.error("args : " + str(args))
    LOG.error("body : " + str(exception.body))

    traceback_str = ""
    if exception.traceback is not None:
        for line in exception.traceback:
            if line.replace(" ", "") != "" and line != "\n":
                traceback_str = traceback_str + "\n" + line

    LOG.error("Traceback : " + traceback_str)
    LOG.error("*" * 67)
    #########################################################

    return error, exception.status
