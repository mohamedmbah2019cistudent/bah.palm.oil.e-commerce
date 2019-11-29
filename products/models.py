from django.db import models
from posts.models import Post
from django.utils import timezone
import datetime


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    Product = models.ForeignKey(Product)
    pub_date = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=100)
    comment = models.TextField(max_length=300)
    rating = models.IntegerField(choices=RATING_CHOICES)
