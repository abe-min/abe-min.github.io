from django.db import models
from django.contrib.auth.models import User



# Extending User Model to settings/profile using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    General = models.BooleanField(default=True)
    Business = models.BooleanField(default=False)
    Entertainment = models.BooleanField(default=False)
    Health = models.BooleanField(default=False)
    Science = models.BooleanField(default=False)
    Sports = models.BooleanField(default=False)
    Technology = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


#class Category(models.Model):
#    General = models.BooleanField(default=False)
#    Business = models.BooleanField(default=False)
#    Entertainment = models.BooleanField(default=False)
#    Health = models.BooleanField(default=False)
#    Science = models.BooleanField(default=False)
#    Sports = models.BooleanField(default=False)
#    Technology = models.BooleanField(default=False)

