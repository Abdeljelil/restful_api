from uuid import uuid1

from aiomotorengine import IntField, StringField, UUIDField

from backend.models.base import BaseModel


class UserModel(BaseModel):

    __collection__ = "user_model"

    uuid = UUIDField(default=uuid1(), required=True)
    name = StringField(required=True)
    user_group_uuid = UUIDField()
    index = IntField()

    def to_dict(self):
        """
        convert fields to dict
        """
        r = dict(
            name=self.name,
            uuid=str(self.uuid),
            user_group_uuid=str(self.user_group_uuid),
            index=self.index
        )
        return r
