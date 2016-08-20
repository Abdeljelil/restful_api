from backend.controllers.base import ControllerBase
from backend.models.user import UserModel


class UserController(ControllerBase):

    model = UserModel

    primary_keys = ["name"]
