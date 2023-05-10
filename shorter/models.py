from django.db import models

from .tools import create_short_uuid

class Url(models.Model):
    id = models.CharField(max_length=8,default=create_short_uuid, primary_key=True, unique=True)
    long_url = models.URLField()
    custom_name = models.CharField(max_length=32, unique=True, blank=True, null=True)

    def get_absolute_url(self):
        if self.custom_name:
            return f"/redirect/{self.custom_name}"
        return f"/redirect/{self.id}"
