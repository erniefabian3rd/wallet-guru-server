from django.db import models

#TO DO: How to properly set up the model for month and year that infinitely increment

class Calendar(models.Model):
    month = models.CharField(max_length=25)
    year = models.CharField(max_length=5)

