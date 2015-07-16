from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)  # primary_key=True
    # user = models.ForeignKey(User, unique=True)  # same effect
    name = models.CharField(max_length=26, blank=True)
    public = models.BooleanField(default=True)
    phone = models.CharField(max_length=15, blank=True)
    contact = models.CharField(max_length=255, blank=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class RegularUser(User):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = 'Regular user account'
        verbose_name_plural = 'Regular user accounts'


class Staff(User):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = 'Staff account'
        verbose_name_plural = 'Staff accounts'