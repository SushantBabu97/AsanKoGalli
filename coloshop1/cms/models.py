from django.db import models
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField


# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField()


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.CharField(max_length=200)
    message = models.TextField()


class Blog(models.Model):
    name = models.CharField(max_length=50)
    image = ImageField()
    author = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now=True)
    content = RichTextField()

    def __str__(self):
        return self.name


class Banner(models.Model):
    image = ImageField()
    intro = models.TextField()
    title = models.CharField(max_length=50)
    end_date = models.DateTimeField(blank=True)
    location = models.CharField(max_length=15)

    def __str__(self):
        return self.title

