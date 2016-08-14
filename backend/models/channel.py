from uuid import uuid1

from aiomotorengine import IntField, StringField, UUIDField

from backend.models import BaseModel


class ChannelModel(BaseModel):

    __collection__ = "channel_model"

    uuid = UUIDField(default=uuid1(), required=True)
    name = StringField(required=True)
    index = IntField()

    def to_dict(self):
        """
        convert fields to dict
        """
        r = dict(
            name=self.name,
            uuid=str(self.uuid),
            index=self.index
        )
        return r
