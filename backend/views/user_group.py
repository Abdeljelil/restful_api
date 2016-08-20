from backend.controllers.user_group import UserGroupController
from backend.views.base import ViewBase


class UserGroupView(ViewBase):

    controller = UserGroupController
