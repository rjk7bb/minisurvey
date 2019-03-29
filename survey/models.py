
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='Player')
    role = models.CharField(max_length=50, default="None")
    room = models.IntegerField(default='0')
    game = models.CharField(max_length=50, default="None")

    "Question Fields"

    "I did ___% of the work for my group."
    q1 = models.IntegerField(default='0')

    "Compared to other people in your group, how would you rank your performance on the simulation?"
    q2 = models.CharField(default='NA', max_length=150)

    "One reason that someone else made a poor decision was:"
    q3 = models.CharField(default='NA', max_length=150)

    "One reason that you made a poor decision was:"
    q4 = models.CharField(default='NA', max_length=150)

    "The person in my group with the most power was:"
    q5 = models.CharField(default='NA', max_length=150)

    "The person in my group that was most effective was:"
    q6 = models.CharField(default='NA', max_length=150)

    "Was there any information that you didn’t share with your group?"
    q7a = models.CharField(default='NA', max_length=150)

    "One piece of information I did not share was:"
    q7b = models.CharField(default='NA', max_length=150)

    "I chose not to share this information because:"
    q7c = models.CharField(default='NA', max_length=150)

    "I would invoke/not invoke the 25th Amendment"
    q10a = models.CharField(default='NA', max_length=150)

    "One reason for this decision is:"
    q10b = models.CharField(default='NA', max_length=150)

    "Another reason is:"
    q10c = models.CharField(default='NA', max_length=150)

    "A final reason is:"
    q10d = models.CharField(default='NA', max_length=150)

    "In general, the above questions in this post-simulation questionnaire were clear."
    q11 = models.CharField(default='NA', max_length=150)

    "'Were any of the post-simulation questions unclear? If so, please let us know what items were unclear."
    q12 = models.CharField(default='NA', max_length=150)

    "Your impression of this Situation Room Experience as a whole is:"
    q13 = models.CharField(default='NA', max_length=150)

    "Are there any changes to this game that you would like to see made? What are they? Any other comments?"
    q14 = models.CharField(default='NA', max_length=150)

    "Your name"
    q15a = models.CharField(default='NA', max_length=150)

    "Your thoughts"
    q15b = models.CharField(default='NA', max_length=150)

    def __str__(self):
        return self.role + "_" + self.game

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Player.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.Player.save()


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


