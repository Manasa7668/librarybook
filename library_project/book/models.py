from django.db import models # type: ignore

# Create your models here.
class Book(models.Model):
    Title=models.CharField(max_length=200)
    Author=models.CharField(max_length=100)
    Year=models.IntegerField()
    Genre =models.CharField(max_length=100)

    
