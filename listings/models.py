from django.db import models

class Listings(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    sqr_feet = models.IntegerField()
    no_bedrooms = models.IntegerField()
    no_bathrooms = models.IntegerField()
    adress = models.CharField(max_length=150)
    # image
    
    def __str__(self):
        return self.title