from tortoise.models import Model
from tortoise import fields
import uuid
from tortoise.contrib.pydantic import pydantic_model_creator


class Websites(Model):
    """
    Model for save website analyzed data in database
    """

    # Fields
    id = fields.IntField(
        pk=True,
    )
    domain = fields.CharField(
        max_length=100,
    )
    code = fields.UUIDField(
        default=uuid.uuid4,
        unique=True,
    )
    created_at = fields.DatetimeField(
        auto_now_add=True,
    )
    analyzed_data = fields.JSONField()

    # Methods
    def __str__(self):
        return str(self.domain)


# register model for pydantic
Website_Pydantic = pydantic_model_creator(Websites, name="Websites")
