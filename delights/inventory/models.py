from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    price_unit = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    unit = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        #return self.name
        return 'There are ' + str(self.quantity) + ' ' + self.unit + ' of ' + self.name + ' reamaining in inventory'
