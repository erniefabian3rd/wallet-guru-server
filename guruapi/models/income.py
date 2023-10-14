from django.db import models

class Income(models.Model):
    merchant = models.CharField(max_length=75)
    date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    amount_received = models.FloatField(blank=True, default=0.00)
    notes = models.CharField(max_length=150)
    income_item = models.ForeignKey("IncomeItem", on_delete=models.CASCADE, related_name="income_input")
    calendar = models.ForeignKey("Calendar", on_delete=models.CASCADE, related_name="expense_date")