from typing import List
from django.shortcuts import get_object_or_404
from ..models import Restaurant, Chef, Review
from ..schemas import RestaurantIn, ChefIn, ReviewIn


class RestaurantService:
    @staticmethod
    def get_all_restaurants() -> List[Restaurant]:
        return Restaurant.objects.all()

    @staticmethod
    def create_restaurant(payload: RestaurantIn) -> Restaurant:
        return Restaurant.objects.create(**payload.dict())


class ChefService:
    @staticmethod
    def get_all_chefs() -> List[Chef]:
        return Chef.objects.all()

    @staticmethod
    def create_chef(payload: ChefIn) -> Chef:
        return Chef.objects.create(**payload.dict())


class ReviewService:
    @staticmethod
    def get_all_reviews() -> List[Review]:
        return Review.objects.select_related('restaurant').all()

    @staticmethod
    def create_review(payload: ReviewIn) -> Review:
        return Review.objects.create(**payload.dict())


class MenuService:
    @staticmethod
    def get_restaurant_menu(restaurant_id: int) -> List[dict]:
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        pizzas = restaurant.pizzas.prefetch_related('ingredients').all()

        menu_items = []
        for pizza in pizzas:
            menu_items.append({
                "id": pizza.id,
                "name": pizza.name,
                "cheese_type": pizza.cheese_type,
                "dough": pizza.get_dough_display(),
                "ingredients": [i.name for i in pizza.ingredients.all()]
            })

        return menu_items