import pytest
from restaurants.models import Restaurant


@pytest.mark.django_db
def test_create_restaurant(client):
    response = client.post(
        "/api/restaurants/",
        {"name": "Pizzeria", "address": "Wall Street 10"},
        content_type="application/json",
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Pizzeria"
    assert Restaurant.objects.count() == 1


@pytest.mark.django_db
def test_list_restaurants(client, sample_restaurant):
    response = client.get("/api/restaurants/")
    assert response.status_code == 200
    data = response.json()
    assert any(r["name"] == sample_restaurant.name for r in data)




@pytest.mark.django_db
def test_get_nonexistent_restaurant(client):
    response = client.get("/restaurants/9999")
    assert response.status_code == 404