import pytest
from restaurants.models import Chef


@pytest.mark.django_db
def test_create_chef(client, sample_restaurant):
    payload = {"name": "Jamie Oliver", "restaurant_id": sample_restaurant.id}
    response = client.post("/api/chefs/", payload, content_type="application/json")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jamie Oliver"
    assert Chef.objects.count() == 1


@pytest.mark.django_db
def test_list_chefs(client, sample_chef):
    response = client.get("/api/chefs/")
    assert response.status_code == 200
    data = response.json()
    assert any(c["name"] == sample_chef.name for c in data)


@pytest.mark.django_db
def test_create_chef_invalid_experience(client):
    data = {"name": "Bad Chef", "experience": -5}
    response = client.post("/chefs/", json=data)
    assert response.status_code == 404