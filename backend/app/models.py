from django.db import models

# Create your models here.
class User(models.Model):
    """
    User model for Django
    The phone is optional.
    """
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self
