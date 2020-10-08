from django.contrib import admin
from .models import *


# Register your models here.

class ProductHasImageInline(admin.TabularInline):
    model = ProductHasImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductHasImageInline,
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductsHasImage)
admin.site.register(ProductHasReview)
admin.site.register(Cart)
