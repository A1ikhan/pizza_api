from enum import Enum
from typing import List, Optional
from ninja import ModelSchema, Schema
from .models import Restaurant, Chef, Pizza, Ingredient, Review

class RestaurantIn(Schema):
    name: str
    address: str


class RestaurantOut(ModelSchema):
    class Config:
        model = Restaurant
        model_fields = ['id', 'name', 'address']


class ChefIn(Schema):
    name: str
    restaurant_id: int


class ChefOut(ModelSchema):
    class Config:
        model = Chef
        model_fields = ['id', 'name']

    @staticmethod
    def resolve_restaurant_id(obj):
        return obj.restaurant.id


class IngredientOut(ModelSchema):
    class Config:
        model = Ingredient
        model_fields = ['id', 'name']
class DoughType(str, Enum):
    THIN = "thin"
    CLASSIC = "classic"
    THICK = "thick"

    @property
    def display_name(self) -> str:
        """Возвращает человекочитаемое название"""
        display_map = {
            DoughType.THIN: "Тонкое",
            DoughType.CLASSIC: "Классическое",
            DoughType.THICK: "Пышное"
        }
        return display_map[self]


class PizzaIn(Schema):
    name: str
    cheese_type: str
    dough: DoughType
    secret_ingredient: str
    restaurant_id: int
    ingredient_ids: List[int] = []


class PizzaOut(ModelSchema):
    ingredients: List[IngredientOut] = []

    class Config:
        model = Pizza
        model_fields = ['id', 'name', 'cheese_type', 'dough', 'secret_ingredient']

    @staticmethod
    def resolve_restaurant_id(obj):
        return obj.restaurant.id
class ReviewIn(Schema):
    restaurant_id: int
    rating: int
    text: str


class ReviewOut(ModelSchema):
    restaurant_name: str

    class Config:
        model = Review
        model_fields = ['id', 'rating', 'text', 'created_at']

    @staticmethod
    def resolve_restaurant_name(obj):
        return obj.restaurant.name



class MenuItem(Schema):
    id: int
    name: str
    cheese_type: str
    dough: DoughType
    dough_display: str
    ingredients: List[str]

    @staticmethod
    def resolve_dough_display(obj: 'Pizza') -> str:
        """Резолвер для человекочитаемого названия теста"""
        return obj.get_dough_display()