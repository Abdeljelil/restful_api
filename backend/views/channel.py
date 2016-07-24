from backend.views import ViewBase
from backend.controllers.channel import ChannelController


class ChannelView(ViewBase):

    controller = ChannelController
