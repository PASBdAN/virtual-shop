from django.db import models
from uuid import uuid4

# Create your models here.

class Products(models.Model):
    id_product = models.UUIDField(primary_key=True, default=uuid4, editable=False)