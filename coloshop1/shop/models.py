from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from django.db.models import Avg
import math


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    details = RichTextField()
    slug = AutoSlugField(populate_from='title')
    image = ImageField(blank=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    shart_intro = models.CharField(max_length=200)
    price = models.IntegerField()
    discount_price = models.IntegerField()
    description = RichTextField()
    additional_information = RichTextField()
    best_seller = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    sale = models.BooleanField()

    def __str__(self):
        return self.title

    def image(self):
        return self.producthasimage_set.first()

    def loop_for_star(self):
        avg = self.producthasreview_set.aggregate(Avg('rating'))
        if avg['rating__avg']:
            return range(int(math.ceil(avg['rating__avg'])))

    class Meta:
        verbose_name_plural = 'Products'


class ProductHasImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = ImageField()


class ProductHasReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    comment = models.TextField()

    def loop_for_star(self):
        return range(self.rating)


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qty = models.IntegerField()
