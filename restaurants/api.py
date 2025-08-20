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










