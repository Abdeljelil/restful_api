from backend.controllers.base import ControllerBase
from backend.models.user_group import UserGroupModel


class UserGroupController(ControllerBase):

    model = UserGroupModel

    primary_keys = ["name"]
