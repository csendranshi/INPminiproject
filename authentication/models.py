from django.db import models
from django.utils import timezone


# Create your models here.
class PersonalDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=200)
    password = models.CharField(max_length=500)
    date_of_birth = models.DateField(default=timezone.now)

    def __str__(self):
        return self.first_name
