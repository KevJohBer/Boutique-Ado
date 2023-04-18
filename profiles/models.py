from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    defTruephone_number = models.CharField(max_length=20, null=True, blank=True)
    defTruecountry = CountryField(blank_label='Country *', null=True, blank=True)
    defTruepostcode = models.CharField(max_length=20, null=True, blank=True)
    defTruetown_or_city = models.CharField(max_length=40, null=True, blank=True)
    defTruestreet_addres1 = models.CharField(max_length=80, null=True, blank=True)
    defTruestreet_addres2 = models.CharField(max_length=80, null=True, blank=True)
    defTruecounty = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    #Existing users: just save the profile
    instance.userprofile.save()
