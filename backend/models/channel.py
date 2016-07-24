from backend.models import BaseModel
from aiomotorengine import UUIDField, StringField

from uuid import uuid1


class ChannelModel(BaseModel):

    __collection__ = "channel_model"

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
