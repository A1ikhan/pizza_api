import pytest
from django.test import Client
from restaurants.models import Restaurant, Chef, Ingredient, Pizza, Review


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def sample_restaurant(db):
    return Restaurant.objects.create(name="Test Restaurant", address="Main Street 123")


@pytest.fixture
def sample_chef(db, sample_restaurant):
    return Chef.objects.create(name="Gordon Ramsay", restaurant=sample_restaurant)


@pytest.fixture
def sample_ingredient(db):
    return Ingredient.objects.create(name="Tomato")


@pytest.fixture
def sample_pizza(db, sample_restaurant, sample_ingredient):
    pizza = Pizza.objects.create(
        name="Pepperoni",
        cheese_type="Cheddar",
        dough="classic",
        secret_ingredient="Secret",
        restaurant=sample_restaurant,
    )
    pizza.ingredients.add(sample_ingredient)
    return pizza


@pytest.fixture
def sample_review(db, sample_restaurant):
    return Review.objects.create(
        restaurant=sample_restaurant,
        rating=5,
        text="Excellent pizza!"
    )
