from django.db import models

# Create your models here.
from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title
