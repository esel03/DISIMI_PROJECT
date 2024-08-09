from django.db import models
from django.contrib.auth.models import User

class Depend(models.Model):
    depend_field = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    views_count = models.BooleanField(default=False)
    data_create = models.DateField()

    class Meta:
        ordering = ['data_create']

    def __str__(self):
        return self.depend_field

    def __str__(self):
        return self.title










# Create your models here.
