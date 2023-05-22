from django.urls import path, include
from rest_framework import routers
from . views import ProductViewSet, CategoryViewSet, CartViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'cart', CartViewSet)


urlpatterns = [
    
    path('', include(router.urls))
    
]