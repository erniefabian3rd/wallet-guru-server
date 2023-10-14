from django.db import models

class IncomeItem(models.Model):
    guru = models.ForeignKey("WalletGuruUser", on_delete=models.CASCADE, related_name="income_poster")
    name = models.CharField(max_length=75)
    income_category = models.ForeignKey("IncomeCategory", on_delete=models.CASCADE, related_name="income_item")
    planned_amount = models.FloatField(blank=True, default=0.00)
    recurring_monthly = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)