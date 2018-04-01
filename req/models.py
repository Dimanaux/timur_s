from django.db import models

# Create your models here.
from django.db.models import TextField


class Request(models.Model):
    head = TextField()
    body = TextField()

    def __str__(self):
        return str(self.head) + ' ' + str(self.body)
