from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
USER_ROLES = [("Admin", "Admin"), ("user", "user")]


# Define a custom user manager
class UserAccountManager(UserManager):

    # override create user method to accept email as username
    def create_user(self, email=None, password=None, **extra_fields):
        return super().create_user(
            email, email=email, password=password, **extra_fields
        )

    # override createsuperuser method to accept email as username
    def create_superuser(self, email=None, password=None, **extra_fields):
        return super().create_superuser(
            email, email=email, password=password, **extra_fields
        )


# define our custom user model
class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to="users/photos", null=True, blank=True)
    role = models.CharField(max_length=40, choices=USER_ROLES, default="user")
    # last_login = models.DateTimeField(null=True)
    USERNAME_FIELD = "email"
    Country = models.CharField(max_length=32)

    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserAccountManager()

    class Meta:
        ordering = ["-date_joined"]
