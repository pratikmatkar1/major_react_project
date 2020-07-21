from django.db import models
from api.validators import validate_password_digit, validate_password_uppercase


# Create your models here.
class UserAPI(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30, validators=[validate_password_digit, validate_password_uppercase])

    def __str__(self):
        return self.email




# Create your models here.
