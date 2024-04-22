from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TotalTrackedTime(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_time_tracked = models.DurationField(default=0)

    def update_total_time_tracked(self):
        # Calculate total time tracked based on sessions
        total_time = self.user.focussession_set.aggregate(total=models.Sum('session_length'))['total']
        self.total_time_tracked = total_time if total_time else 0
        self.save()

    def __str__(self):
        return f"Total Tracked Time for {self.user.username}"


class Achievement(models.Model):
    achievement_name = models.CharField(max_length=100)
    achievement_description = models.TextField()
    unlock_threshold = models.IntegerField()

    def __str__(self):
        return self.achievement_name


class FocusSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    session_length = models.DurationField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.user.totaltrackedtime.update_total_time_tracked()

    def __str__(self):
        return f"Focus Session for {self.user.username}"


class Friend(models.Model):
    user1 = models.ForeignKey(User, related_name='user1_friends', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='user2_friends', on_delete=models.CASCADE)
    friendship_status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user1.username} - {self.user2.username}"


class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s achievement: {self.achievement.achievement_name}"
