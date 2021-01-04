# goes in app directory

# post_save signal that's fired after object is saved
# post_save after user created
from django.db.models.signals import post_save

#User is signal "sender"
from django.contrib.auth.models import User

# receiver is fn that gets signal and performs task
from django.dispatch import receiver

from .models import Profile

# want a user Profile to be created for each new profile


# run everytime a user is created
# when a User is save, then send post_save signal - and the create_profile fn will run
# instance of User, and if it's created
@receiver(post_save, sender=User)  
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



# run everytime a user is created
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
