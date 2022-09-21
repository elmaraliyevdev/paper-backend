from django.db import models
from accounts.models import User
from clients.models import Client


class Project(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=150, unique=True, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    currency = models.CharField(max_length=150, unique=True, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_hourly = models.BooleanField(default=False)

    def __str__(self):
        return self.name
