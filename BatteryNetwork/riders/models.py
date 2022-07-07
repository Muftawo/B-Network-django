from django.db import models
from batteries.models import Battery


# Create your models here.
class Rider(models.Model):
    def __init__(self):
        pass
    categories = (
        ('O', 'Okada'),
        ('P', 'Personal Commuter'),
        ('F', 'Fleet Rider')

    )
    id = models.AutoField(primary_key=True)
    rider_category = models.CharField(max_length=2, choices=categories)
    registered_on = models.DateTimeField(auto_now_add=True)
    last_swap = models.DateTimeField()
    current_batteries = models.ManyToManyField(Battery), models.ManyToManyField(Battery)



