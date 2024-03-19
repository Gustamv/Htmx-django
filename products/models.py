from django.db import models

# Create your models here.
#10- create the class for the products name and price on the db
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name
