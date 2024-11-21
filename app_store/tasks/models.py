from django.db import models
from datetime import time

class Task(models.Model):
    title = models.CharField(max_length=35, blank=False, unique=True, null=False)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField( null=True, blank=True)
    due_time = models.TimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title}'


class Item(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    obtained = models.BooleanField(default=False)
    budgeted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cheapest_price_sourced = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sourced_store = models.CharField(max_length=100, null=True, blank=True)
    product_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name} for {self.task.title}'