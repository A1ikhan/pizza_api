import pytest
from restaurants.models import Review


@pytest.mark.django_db
def test_create_review(client, sample_restaurant):
    payload = {"restaurant_id": sample_restaurant.id, "rating": 4, "text": "Good food!"}
    response = client.post("/api/reviews/", payload, content_type="application/json")
    assert response.status_code == 200
    data = response.json()
    assert data["rating"] == 4
    assert Review.objects.count() == 1


@pytest.mark.django_db
def test_list_reviews(client, sample_review):
    response = client.get("/api/reviews/")
    assert response.status_code == 200
    data = response.json()
    assert any(r["text"] == sample_review.text for r in data)

@pytest.mark.django_db
def test_create_review_invalid_rating(client):
    data = {"text": "Too salty", "rating": 10}  # рейтинг вне диапазона
    response = client.post("/reviews/", json=data)
    assert response.status_code == 404