from django.db import models
import uuid

class Avto(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),blank=False,null=False,primary_key=True,editable=False)
    price = models.CharField(max_length=100,null=True,blank=True)
    year = models.CharField(max_length=100,null=False,blank=True)
    model = models.CharField(max_length=100,null=False,blank=True)
    info = models.TextField(null=True,blank=True)
