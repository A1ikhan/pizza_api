import pytest


@pytest.mark.django_db
def test_list_ingredients(client, sample_ingredient):
    response = client.get("/api/ingredients/")
    assert response.status_code == 200
    data = response.json()
    assert any(i["name"] == sample_ingredient.name for i in data)


@pytest.mark.django_db
def test_create_ingredient_empty_name(client):
    data = {"name": ""}
    response = client.post("/ingredients/", json=data)
    assert response.status_code == 404


