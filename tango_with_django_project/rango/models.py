"""For models Ragno app."""
from django.db import models


# Create your models here.

class Category(models.Model):
    """docstring for Category."""

    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

        def __str__(self):
            return self.name


class Page(models.Model):
    """Explanation about page-model."""

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
