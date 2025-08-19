from django.contrib import admin
from .models import Restaurant, Chef, Pizza, Ingredient, Review

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant')

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'cheese_type', 'get_dough_display', 'restaurant')
    filter_horizontal = ('ingredients',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'rating', 'created_at')