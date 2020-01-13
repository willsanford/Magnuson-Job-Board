from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Profile model that has a one-to-one relation with the out of the box user model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # here we can add things like saved jobs and others 
    


#automatically creates and saves the extra data ascociated with the user on creation and whatever changes are made
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()