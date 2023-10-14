from django.db import models

class IncomeCategory(models.Model):
    name = models.CharField(max_length=75)