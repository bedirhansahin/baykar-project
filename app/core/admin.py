from django.contrib import admin

from . models import Products, Type, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'producer']
    search_fields = ['producer', 'name']
