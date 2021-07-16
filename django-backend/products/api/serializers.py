from rest_framework import serializers
from products import models



class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'