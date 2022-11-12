from django.contrib import admin

from django.utils.safestring import mark_safe
from .models import ProductModel,  ProductSizeModel, ProductCategoryModel, ProductColorModel, ProductTagModel, ProductBrandModel
from .forms import ColorForm

@admin.register(ProductBrandModel)
class ProductModelModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['code']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'real_price', 'price', 'discount']
    list_display_links = ['id', 'title', 'price', 'discount']
    list_filter = ['created_at']
    search_fields = ['title']
    readonly_fields = ['real_price', 'created_at']


@admin.register(ProductCategoryModel)
class ProductColorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ProductColorModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_code', 'code']
    list_display_links = ['id', 'code']
    search_fields = ['title']
    form = ColorForm

    def get_code(self, obj):
        text = '&nbsp'
        return mark_safe(f'<div style="background-color: {obj.code}; width:70px">{text}</div>')


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['code']


@admin.register(ProductSizeModel)
class ProductSizeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
