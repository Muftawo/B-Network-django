import sys
from django.db import models
from riders.models import Rider


# Create your models here.
class Battery(models.Model):
    def __init__(self,id):
        print(self.id)
        pass
    cells = (
        ("NMC", "Nickel Manganese Cobalt"),
        ("LFP", "Lithium Iron Phosphate")
    )

    id = models.AutoField(primary_key=True)
    battery_code = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    cell_type = models.CharField(max_length=5, choices=cells)
    batch_num = models.IntegerField()
    current_user = models.ManyToManyField(Rider)
    soc = models.FloatField()
    soh = models.FloatField()
    latitude = models.FloatField()
    Longitude = models.FloatField()
    iot_live = models.BooleanField()










