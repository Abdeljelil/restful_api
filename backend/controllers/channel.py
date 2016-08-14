from backend.controllers import ControllerBase
from backend.models.channel import ChannelModel


class ChannelController(ControllerBase):

    model = ChannelModel

    primary_keys = ["name"]
