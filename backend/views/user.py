from backend.controllers.user import UserController
from backend.views.base import ViewBase


class UserView(ViewBase):

    controller = UserController
