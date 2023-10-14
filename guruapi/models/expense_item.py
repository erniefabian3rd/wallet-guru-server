from django.db import models

class ExpenseItem(models.Model):
    guru = models.ForeignKey("WalletGuruUser", on_delete=models.CASCADE, related_name="expense_poster")
    name = models.CharField(max_length=75)
    expense_category = models.ForeignKey("ExpenseCategory", on_delete=models.CASCADE, related_name="expense_item")
    planned_amount = models.FloatField(blank=True, default=0.00)
    recurring_monthly = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)