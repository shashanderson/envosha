from django.db import models
from django.utils import timezone

# Create your models here.


class Form(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title