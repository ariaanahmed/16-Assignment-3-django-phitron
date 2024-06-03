from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    select_category = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.category_name
