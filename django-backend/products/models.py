from django.db import models
from helpers.models import TrackingModel
from uuid import uuid4

# Create your models here.

def upload_image_product(instance, filename):
    '''
    Função necessária para evitar ter nomes de arquivos duplicados:
    Cocatena-se o id do produto/objeto no nome do arquivo.
    '''
    return f'{instance.id_product}-{filename}'

class Products(TrackingModel):
    id_product = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=1020, blank=False)
    price = models.FloatField(blank=False)
    image = models.ImageField(upload_to=upload_image_product)