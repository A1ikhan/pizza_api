from typing import List

from django.shortcuts import get_object_or_404

from restaurants.models import Restaurant
from restaurants.schemas import MenuItem, DoughType


class MenuService:
    @staticmethod
    def get_restaurant_menu(restaurant_id: int) -> List[dict]:
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        pizzas = restaurant.pizzas.prefetch_related('ingredients').all()

        menu_items = []
        for pizza in pizzas:
            menu_item = MenuItem(
                id=pizza.id,
                name=pizza.name,
                cheese_type=pizza.cheese_type,
                dough=DoughType(pizza.dough),
                dough_display=pizza.get_dough_display(),   # ✅ добавляем
                ingredients=[i.name for i in pizza.ingredients.all()]
            )
            menu_items.append(menu_item)

        return menu_items


def test_create_menu_with_nonexistent_pizza(client):
    data = {"pizza_id": 999, "restaurant_id": 1, "price": 12.0}
    response = client.post("/menu/", json=data)
    assert response.status_code == 404

def test_create_menu_with_invalid_price(client):
    data = {"pizza_id": 1, "restaurant_id": 1, "price": -5}
    response = client.post("/menu/", json=data)
    assert response.status_code == 404