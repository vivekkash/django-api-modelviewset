from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from . models import Product, Category, Cart
from . serializers import ProductSerializer, CategorySerializer, CartSerializer

# Create your views here
class ProductViewSet(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    #/category/<id>/products
    @action(detail=True, methods=['GET'])
    def products(self, request, pk=None):
        
        try: 
            category = Category.objects.get(pk=pk)
            products_data = Product.objects.filter(category=category)
            product_serializers = ProductSerializer(products_data, many=True, context={'request':request})
            
            
            return Response(product_serializers.data)
        except Exception as e:
            
            return Response({'error': 'Product data not found'})
    
    
class CartViewSet(viewsets.ModelViewSet):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer        