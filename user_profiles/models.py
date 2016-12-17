from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # Store the Django User
    # Its a one to one field that uses
    # the same data type as the django user
    user = models.OneToOneField(User)
    bio = models.TextField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return self.user.username


# Now store the data in db as soon as the profile is created

from django.db.models.signals import post_save
from django.dispatch import receiver

# If the User is sending a post_save signal then store the data
# in the database
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)