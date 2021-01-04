from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Create your models here.


class Profile(models.Model):

    # when a user is deleted , then also delete profile
    # but if you delete profile, it won't delete user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # default user for any user, and an upload directory
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # used when we print out profile
    def __str__(self):
        return f'{self.user.username} Profile'

    # override save to alter image save

    def save(self):
        # run parent's save method which is the default method if an image is saved
        super().save()

        # open image of current instance
        img = Image.open(self.image.path)

        # max size of image we display is around 125 px - but choose 300 as a good default resize
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
