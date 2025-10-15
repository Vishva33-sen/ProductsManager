from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.site_header = "MyApp Admin"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description','type')
    search_fields = ('name',)
    list_filter = ('price',)

