from tornado.web import RequestHandler
from tornado import gen
from tornado.escape import json_decode

from backend.utils.decorators import view_wrapper


class ViewBase(RequestHandler):
    controller = None

    @view_wrapper
    @gen.coroutine
    def get(self, uuid=None):
        """
        get data from database override this method
        if you want to customize the request.
        """
        if uuid is not None:
            uuid = uuid.split("/")[-1]

        objects = yield from self.controller.list(uuid)
        data = {}
        for object_ in objects:
            data[str(object_.uuid)] = object_.to_dict()

        return data

    @view_wrapper
    @gen.coroutine
    def post(self, post_url=None):
        """
        update data in database or
        get data according give query
        """

        if post_url == "/search":
            data = json_decode(self.request.body)
            objects = yield from self.controller.search(**data)

        else:
            data = json_decode(self.request.body)

            objects = []
            for uuid, values in data.items():
                obj = yield from self.controller.update(uuid, **values)
                objects.append(obj)

        data = {}
        for object_ in objects:
            data[str(object_.uuid)] = object_.to_dict()

        return data

    @view_wrapper
    @gen.coroutine
    def put(self, post_url=None):
        """
        create new object in database
        """
        data = json_decode(self.request.body)
        print("in put request data : {}".format(data))
        obj = yield from self.controller.create(**data)

        response = obj.render_to_response()
        return response

    @view_wrapper
    @gen.coroutine
    def delete(self, post_url):

        uuid = post_url.split("/")[-1]

        obj = yield from self.controller.delete(uuid)

        response = obj.render_to_response()
        return response
