from backend.models.channel import ChannelModel
from backend.controllers import ControllerBase


class ChannelController(ControllerBase):
    model = ChannelModel

    primary_keys = ["name"]
