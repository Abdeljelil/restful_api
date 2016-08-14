from aiomotorengine import Document
from backend.settings import LOG


class BaseModel(Document):
    """
        Parent class of all Models
    """

    def to_dict(self):
        """ override this method for subclass model"""
        return {}

    def render_to_response(self):
        """
        base format of response
        {
        uuid :{
                name : "myame",
                lastname: "mylastname"
                }
        }
        """
        return {str(self.uuid): self.to_dict()}
