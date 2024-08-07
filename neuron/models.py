from django.db import models
from django.contrib.auth.models import User

class Depend(models.Model):
    depend_field = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    views_count = models.PositiveIntegerField()
    data_create = models.DateField()

    class Meta:
        ordering = ['data_create']

    def __str__(self):
        return self.title

    def __str__(self):
        return self.views_count

    def __str__(self):
        return self.data_create








# Create your models here.
