
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="profile")
    role = models.CharField(max_length=50, default="None")
    room = models.IntegerField(default='0', max_length=2)
    game = models.CharField(max_length=50, default="None")

    def __str__(self):
        return self.role + "_" + self.game

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Player.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Question(models.Model):
    question_text = models.CharField(max_length=200, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_text = models.TextField(default=None)

    def __str__(self):
        return self.response_text


