from django.db import models
from django.contrib.auth.models import User

class WalletGuruUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    financial_goal = models.CharField(max_length=150)
    created_on = models.DateField(null=False, blank=False, auto_now=False, auto_now_add=True)