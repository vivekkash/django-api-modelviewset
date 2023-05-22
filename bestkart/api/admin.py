from django.contrib import admin
from  . models import Product, Category, Cart
# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','category')
    list_filter = ('category',)
    search_fields = ('name',)





admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Cart)