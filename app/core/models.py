from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# User model
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


# UAV type model
class Type(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# UAV Model
class Products(models.Model):
    producer = models.CharField(max_length=150)
    name = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.TextField()
    date_of_production = models.DateField()
    weight = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    in_stock = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Unmanned Aerial Vehicle'
        verbose_name_plural = 'Unmanned Aerial Vehicles'

    def __str__(self):
        return self.name
