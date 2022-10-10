from django.db import models
from products import models

# Create your models here.

class Review(models.models.Model):
    review_text = models.models.CharField(max_length=255)
    rating = models.models.IntegerField()
    name = models.models.CharField(max_length=50, default='NAME')
    product = models.models.ForeignKey(models.Product, on_delete=models.models.CASCADE)
    