from django.contrib.auth.models import AbstractUser
from django.db import models

# https://qiita.com/keita_gawahara/items/e534178d9ae89872ebab
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    age = models.IntegerField('age', blank=True, null=True)

    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'
    



# class FriendShip(models.Model):
#     pass
