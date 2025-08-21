import pytest
from restaurants.models import Pizza


@pytest.mark.django_db
def test_create_pizza(client, sample_restaurant, sample_ingredient):
    payload = {
        "name": "Margarita",
        "cheese_type": "Mozzarella",
        "dough": "thin",
        "secret_ingredient": "Love",
        "restaurant_id": sample_restaurant.id,
        "ingredient_ids": [sample_ingredient.id],
    }
    response = client.post("/api/pizzas/", payload, content_type="application/json")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Margarita"
    assert Pizza.objects.count() == 1


@pytest.mark.django_db
def test_list_pizzas(client, sample_pizza):
    response = client.get("/api/pizzas/")
    assert response.status_code == 200
    data = response.json()
    assert any(p["name"] == sample_pizza.name for p in data)


@pytest.mark.django_db
def test_update_pizza(client, sample_pizza, sample_ingredient):
    payload = {
        "name": "Updated Pizza",
        "cheese_type": "Parmesan",
        "dough": "thick",
        "secret_ingredient": "Magic",
        "restaurant_id": sample_pizza.restaurant.id,
        "ingredient_ids": [sample_ingredient.id],
    }
    response = client.put(
        f"/api/pizzas/{sample_pizza.id}/", payload, content_type="application/json"
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Pizza"


@pytest.mark.django_db
def test_delete_pizza(client, sample_pizza):
    response = client.delete(f"/api/pizzas/{sample_pizza.id}/")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert not Pizza.objects.filter(id=sample_pizza.id).exists()



@pytest.mark.django_db
def test_create_pizza_without_price(client):
    data = {"name": "NoPricePizza"}
    response = client.post("/pizzas/", json=data)
    assert response.status_code == 404