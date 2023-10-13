from django.db import models

# Create your models here.

class Payment(models.Model):
    username = models.CharField(max_length=255)
    amoun_money = models.IntegerField()
    comment = models.CharField(max_length=255, null=True, blank=True)