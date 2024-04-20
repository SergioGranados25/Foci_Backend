from django.db import models
from django.contrib.auth.models import User

class Achievement(models.Model):
    achievement_name = models.CharField(max_length=100)
    achievement_description = models.TextField()
    unlock_threshold = models.IntegerField()

class FocusSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    session_length = models.DurationField()

class Friend(models.Model):
    user1 = models.ForeignKey(User, related_name='user1_friends', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='user2_friends', on_delete=models.CASCADE)
    friendship_status = models.CharField(max_length=20)

class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)