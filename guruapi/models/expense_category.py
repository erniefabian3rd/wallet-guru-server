from django.db import models

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=75)