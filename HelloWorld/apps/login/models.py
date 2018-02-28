from django.db import models


# Create your models here.

class Test(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    first_module = models.CharField(max_length=30, default="News")
