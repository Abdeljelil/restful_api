import asyncio

from backend.utils.exceptions import (BadParametersError, ConflictError,
                                      ResourceNotFoundError)


class ControllerBase(object):

    model = None
    # we assume that for each model we have uuid
    # field as required and auto generated
    primary_keys = ["uuid"]

    @classmethod
    @asyncio.coroutine
    def list(cls, uuid=None):
        """
        get all data or get by uuid if "uuid" it is not None
        """
        try:
            if uuid is None or uuid == "":
                # get all data
                objects = yield from cls.model.objects.find_all()
            else:
                objects = yield from cls.model.objects.filter(
                    uuid=uuid
                ).find_all()
        except TypeError:
            return []

        return objects

    @classmethod
    @asyncio.coroutine
    def check_if_exist(cls, **kwargs):
        """
        check primary keys if the are already exist
        in database and raise ConflictError
        """
        filter_by = {
            key: kwargs[key]
            for key in kwargs.keys()
            if key in cls.primary_keys
        }

        result = yield from cls.search(**filter_by)

        if result != []:
            raise ConflictError(
                "Object already exist in database, primary kyes : {}".format(
                    cls.primary_keys
                )
            )

    @classmethod
    def pre_create(cls, **kwargs):
        """
        override this method if you want to put default values
        for some fields before the creation or to run some action.
        you can override this method with classic way or coroutine
        """
        return kwargs

    @classmethod
    def post_create(cls, **kwargs):
        """
        override this method if you want to
        run action after the creation in the database.
        you can override this method with classic way or coroutine
        """
        pass

    @classmethod
    @asyncio.coroutine
    def create(cls, **kwargs):
        """
        create new object in database
        """

        obj = cls.model(**kwargs)

        kwargs["uuid"] = str(obj.uuid)

        if asyncio.iscoroutinefunction(cls.pre_create) is True:
            kwargs = yield from cls.pre_create(**kwargs)
        else:
            kwargs = cls.pre_create(**kwargs)

        # checking the primary keys if they are exist
        # raise ConflictError if object is already exist
        yield from cls.check_if_exist(**kwargs)

        yield from obj.save()

        if asyncio.iscoroutinefunction(cls.post_create) is True:
            yield from cls.post_create(**kwargs)
        else:
            cls.post_create(**kwargs)

        return obj

    @classmethod
    def pre_update(cls, uuid, **kwargs):
        """
        override this method if you want to apply some actions
        before the update in the database
        you can override this method with classic way or coroutine
        """

        return kwargs

    @classmethod
    def post_update(cls, uuid, **kwargs):
        """
        override this method if you want to apply some actions
        after the update in the database
        you can override this method with classic way or coroutine
        """
        pass

    @classmethod
    @asyncio.coroutine
    def update(cls, uuid, **kwargs):
        """
        update object in database
        """

        objs = yield from cls.list(uuid)
        obj = objs[0]

        if asyncio.iscoroutinefunction(cls.pre_update) is True:
            kwargs = yield from cls.pre_update(uuid, **kwargs)
        else:
            kwargs = cls.pre_update(uuid, **kwargs)

        for key in kwargs.keys():
            if hasattr(obj, key):
                setattr(obj, key, kwargs[key])

        new_obj = yield from obj.save()

        if asyncio.iscoroutinefunction(cls.post_update) is True:
            kwargs = yield from cls.post_update(uuid, **kwargs)
        else:
            kwargs = cls.post_update(uuid, **kwargs)
        return new_obj

    @classmethod
    def pre_delete(cls, uuid):
        """
        override this method if you want to apply some actions
        before the delete
        you can override this method with classic way or coroutine
        """

        pass

    @classmethod
    def post_delete(cls, uuid):
        """
        override this method if you want to apply some actions
        after the delete
        you can override this method with classic way or coroutine
        """
        pass

    @classmethod
    @asyncio.coroutine
    def delete(cls, uuid):
        """
        delete object from database by uuid
        """

        if uuid is None or uuid is "":
            raise BadParametersError("uuid is None")

        objs = yield from cls.list(uuid)
        if len(objs) == []:
            raise ResourceNotFoundError(
                "No Resouce found with uuid {}".format(
                    uuid))
        obj = objs[0]

        if asyncio.iscoroutinefunction(cls.pre_delete) is True:
            yield from cls.pre_delete(uuid)
        else:
            cls.pre_delete(uuid)

        yield from obj.delete()

        if asyncio.iscoroutinefunction(cls.post_delete) is True:
            yield from cls.post_delete(uuid)
        else:
            cls.post_delete(uuid)

        return obj

    @classmethod
    @asyncio.coroutine
    def search(cls, **kwargs):
        try:
            objects = yield from cls.model.objects.filter(
                **kwargs
            ).find_all()
        except TypeError:
            return []
        return objects
