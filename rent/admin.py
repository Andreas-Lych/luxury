from django.contrib import admin

from rent.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "created_at", "color", "gearbox", "fuel",)
    fields = ("title", "image", "price", "created_at", "color", "gearbox", "fuel",)
    readonly_fields = ("created_at",)
    search_fields = ("title", "description")

