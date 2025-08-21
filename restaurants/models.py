from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Chef(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='chef'
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    DOUGH_CHOICES = [
        ('thin', 'Тонкое'),
        ('classic', 'Классическое'),
        ('thick', 'Пышное'),
    ]

    name = models.CharField(max_length=100)
    cheese_type = models.CharField(max_length=100)
    dough = models.CharField(max_length=10, choices=DOUGH_CHOICES)
    secret_ingredient = models.CharField(max_length=100)
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='pizzas'
    )
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name


class Review(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"Review for {self.restaurant.name} ({self.rating}/5)"