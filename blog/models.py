from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


# Posts - posts themselves
class Post(models.Model):
    title = models.CharField(max_length=100)  # CharField is up to 255 char
    content = models.TextField()  # Textfield has up to 4GB

    # user who created the post - one user to many posts
    # if a user is deleted => also delete their post  (if you delete a post, it's not going to delete an author/user)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # no paranthesis on timezone.now, just passing function
    date_posted = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
# Users - authors of posts
# django already has a users
