from django.db import models
from accounts.models import User
from clients.models import Client


class Contract(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name
