from typing import List
from django.shortcuts import get_object_or_404
from ..models import Pizza, Ingredient
from ..schemas import PizzaIn


class PizzaService:
    @staticmethod
    def get_all_pizzas() -> List[Pizza]:
        return Pizza.objects.all()

    @staticmethod
    def create_pizza(payload: PizzaIn) -> Pizza:
        data = payload.dict()
        ingredient_ids = data.pop('ingredient_ids')
        pizza = Pizza.objects.create(**data)
        pizza.ingredients.set(ingredient_ids)
        return pizza

    @staticmethod
    def update_pizza(pizza_id: int, payload: PizzaIn) -> Pizza:
        pizza = get_object_or_404(Pizza, id=pizza_id)
        data = payload.dict()
        ingredient_ids = data.pop('ingredient_ids')

        for attr, value in data.items():
            setattr(pizza, attr, value)
        pizza.save()
        pizza.ingredients.set(ingredient_ids)
        return pizza

    @staticmethod
    def delete_pizza(pizza_id: int) -> bool:
        pizza = get_object_or_404(Pizza, id=pizza_id)
        pizza.delete()
        return True


class IngredientService:
    @staticmethod
    def get_all_ingredients() -> List[Ingredient]:
        return Ingredient.objects.all()