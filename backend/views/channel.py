from backend.controllers.channel import ChannelController
from backend.views import ViewBase


class ChannelView(ViewBase):

    controller = ChannelController
