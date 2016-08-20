from uuid import uuid1

from aiomotorengine import StringField, UUIDField

from backend.models.base import BaseModel


class UserGroupModel(BaseModel):

    __collection__ = "user_group_model"

    uuid = UUIDField(default=uuid1(), required=True)
    name = StringField(required=True)

    def to_dict(self):
        """
        convert fields to dict
        """
        r = dict(
            name=self.name,
            uuid=str(self.uuid)
        )
        return r
