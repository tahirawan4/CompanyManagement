from django.db import models

from core.models import BaseModel


class Item(BaseModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ItemPackaging(BaseModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
