from django.db import models

from .tools import create_short_uuid

class Url(models.Model):
    id = models.CharField(max_length=8,default=create_short_uuid, primary_key=True, unique=True)
    long_url = models.URLField()

    def get_absolute_url(self):
        return f"/redirect/{self.id}"
