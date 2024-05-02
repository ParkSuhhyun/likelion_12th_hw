from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(null=True, max_length=10)
    birth=models.TextField(max_length=8)
    grade = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1)


# Create your models here.
