from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','product_image','price','description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductAdmin)
