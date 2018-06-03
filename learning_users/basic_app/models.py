from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):

    # Directly links this model to User model that is built in
    # This wouls be a column in the table linking to the corresponding User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # This is the stuff we want to add to user table
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    # username is an attribute of the default User model
    def __str__(self):
        return self.user.username
