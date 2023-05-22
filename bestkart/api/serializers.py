from rest_framework import serializers
from . models import Product, Category, Cart

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model=Product
        fields='__all__' # to include all fields or specific in tuples ('id','name')
        

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model=Category
        fields='__all__'
        
        
class CartSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    
    class Meta:
        model=Cart
        fields='__all__'                