# your_app/admin.py
from django.contrib import admin
from .models import ProductReview

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('score', 'product_id', 'label', 'review')
    search_fields = ('product_id', 'label', 'review')
