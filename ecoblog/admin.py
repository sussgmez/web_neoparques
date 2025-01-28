from django.contrib import admin
from .models import Category, ProtectedArea


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(ProtectedArea)
class ProtectedAreaAdmin(admin.ModelAdmin):
    pass

