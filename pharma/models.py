from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


class Cure(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=30)
    price = models.IntegerField(null=False)
    description = models.TextField(max_length=70)
    amount = models.IntegerField()
    cure_location = models.TextField(null=False, default='00000000',)
    available = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


class UserCure(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    cure = models.ForeignKey(Cure, on_delete=CASCADE)



