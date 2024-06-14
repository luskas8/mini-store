from django.db import models
from utils.db import ModelDefault
from uuid import uuid4

class BaseProduct(ModelDefault):
    name = models.CharField(max_length=120)
    external_id = models.UUIDField(editable=False, default=uuid4, primary_key=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

        ordering = ['id']