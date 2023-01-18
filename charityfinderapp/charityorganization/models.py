from django.db import models

# Create your models here.

class Charityorg(models.Model):
    reg_number = models.CharField(max_length=7)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    contact = models.IntegerField(20)

    class Meta:
        db_table = "charityorg"