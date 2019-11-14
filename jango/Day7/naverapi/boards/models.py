from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    created_by = models.CharField(max_length=10, null = True)




    