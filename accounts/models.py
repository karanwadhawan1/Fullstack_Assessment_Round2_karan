from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass  # username and password already included in AbstractUser