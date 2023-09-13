from django.db import models


class BaseModel(models.Model):
    """
    Base app model.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
