from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Category(models.Model):
    
    name=models.CharField(max_length=100, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        ordering = ['name']
        
    
class Product(models.Model):
    
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    description=models.TextField()
    image=models.URLField()
    active=models.BooleanField(default=True)
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        ordering = ['name']

class Cart(models.Model):
    
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cart')
    created_at=models.DateTimeField(auto_now_add=True)
        
    def __str__(self) -> str:
        return f'{self.name}'    
    