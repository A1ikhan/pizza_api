from ninja import NinjaAPI, Router
from typing import List
from .services import (
    RestaurantService, ChefService, PizzaService,
    IngredientService, ReviewService, MenuService
)
from .schemas import (
    RestaurantIn, RestaurantOut,
    ChefIn, ChefOut,
    PizzaIn, PizzaOut,
    IngredientOut,
    ReviewIn, ReviewOut,
    MenuItem
)

api = NinjaAPI()




@api.get("/restaurants/", response=List[RestaurantOut])
def list_restaurants(request):
    return RestaurantService.get_all_restaurants()


@api.post("/restaurants/", response=RestaurantOut)
def create_restaurant(request, payload: RestaurantIn):
    return RestaurantService.create_restaurant(payload)


@api.get("/chefs/", response=List[ChefOut])
def list_chefs(request):
    return ChefService.get_all_chefs()


@api.post("/chefs/", response=ChefOut)
def create_chef(request, payload: ChefIn):
    return ChefService.create_chef(payload)


@api.get("/pizzas/", response=List[PizzaOut])
def list_pizzas(request):
    return PizzaService.get_all_pizzas()


@api.post("/pizzas/", response=PizzaOut)
def create_pizza(request, payload: PizzaIn):
    return PizzaService.create_pizza(payload)


@api.put("/pizzas/{pizza_id}/", response=PizzaOut)
def update_pizza(request, pizza_id: int, payload: PizzaIn):
    return PizzaService.update_pizza(pizza_id, payload)


@api.delete("/pizzas/{pizza_id}/")
def delete_pizza(request, pizza_id: int):
    PizzaService.delete_pizza(pizza_id)
    return {"success": True}


@api.get("/ingredients/", response=List[IngredientOut])
def list_ingredients(request):
    return IngredientService.get_all_ingredients()


@api.get("/reviews/", response=List[ReviewOut])
def list_reviews(request):
    return ReviewService.get_all_reviews()


@api.post("/reviews/", response=ReviewOut)
def create_review(request, payload: ReviewIn):
    return ReviewService.create_review(payload)


@api.get("/restaurants/{restaurant_id}/menu/", response=List[MenuItem])
def get_restaurant_menu(request, restaurant_id: int):
    return MenuService.get_restaurant_menu(restaurant_id)










# from ninja import NinjaAPI, Router
# from typing import List
# from django.shortcuts import get_object_or_404
# from .models import Restaurant, Chef, Pizza, Ingredient, Review
# from .schemas import (
#     RestaurantIn, RestaurantOut,
#     ChefIn, ChefOut,
#     PizzaIn, PizzaOut,
#     IngredientOut,
#     ReviewIn, ReviewOut,
#     MenuItem
# )
#
# api = NinjaAPI()
#
#
# @api.get("/restaurants/", response=List[RestaurantOut])
# def list_restaurants(request):
#     return Restaurant.objects.all()
#
#
# @api.post("/restaurants/", response=RestaurantOut)
# def create_restaurant(request, payload: RestaurantIn):
#     restaurant = Restaurant.objects.create(**payload.dict())
#     return restaurant
#
#
# @api.get("/chefs/", response=List[ChefOut])
# def list_chefs(request):
#     return Chef.objects.all()
#
#
# @api.post("/chefs/", response=ChefOut)
# def create_chef(request, payload: ChefIn):
#     chef = Chef.objects.create(**payload.dict())
#     return chef
#
#
# @api.get("/pizzas/", response=List[PizzaOut])
# def list_pizzas(request):
#     return Pizza.objects.all()
#
#
# @api.post("/pizzas/", response=PizzaOut)
# def create_pizza(request, payload: PizzaIn):
#     data = payload.dict()
#     ingredient_ids = data.pop('ingredient_ids')
#     pizza = Pizza.objects.create(**data)
#     pizza.ingredients.set(ingredient_ids)
#     return pizza
#
#
# @api.put("/pizzas/{pizza_id}/", response=PizzaOut)
# def update_pizza(request, pizza_id: int, payload: PizzaIn):
#     pizza = get_object_or_404(Pizza, id=pizza_id)
#     data = payload.dict()
#     ingredient_ids = data.pop('ingredient_ids')
#     for attr, value in data.items():
#         setattr(pizza, attr, value)
#     pizza.save()
#     pizza.ingredients.set(ingredient_ids)
#     return pizza
#
#
# @api.delete("/pizzas/{pizza_id}/")
# def delete_pizza(request, pizza_id: int):
#     pizza = get_object_or_404(Pizza, id=pizza_id)
#     pizza.delete()
#     return {"success": True}
#
#
# @api.get("/ingredients/", response=List[IngredientOut])
# def list_ingredients(request):
#     return Ingredient.objects.all()
#
#
# @api.get("/reviews/", response=List[ReviewOut])
# def list_reviews(request):
#     return Review.objects.select_related('restaurant').all()
#
#
# @api.post("/reviews/", response=ReviewOut)
# def create_review(request, payload: ReviewIn):
#     review = Review.objects.create(**payload.dict())
#     return review
#
#
# @api.get("/restaurants/{restaurant_id}/menu/", response=List[MenuItem])
# def get_restaurant_menu(request, restaurant_id: int):
#     restaurant = get_object_or_404(Restaurant, id=restaurant_id)
#     pizzas = restaurant.pizzas.prefetch_related('ingredients').all()
#
#     menu_items = []
#     for pizza in pizzas:
#         menu_items.append({
#             "id": pizza.id,
#             "name": pizza.name,
#             "cheese_type": pizza.cheese_type,
#             "dough": pizza.get_dough_display(),
#             "ingredients": [i.name for i in pizza.ingredients.all()]
#         })
#
#     return menu_items