from rest_framework import serializers
from .models import Producto
# Conviente los datos a JSON creando un archivo
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields='__all__'