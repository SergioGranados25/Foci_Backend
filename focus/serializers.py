from rest_framework import serializers
from .models import Achievement, FocusSession, Friend, UserAchievement, TotalTrackedTime

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class FocusSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FocusSession
        fields = '__all__'

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'

class UserAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAchievement
        fields = '__all__'

class TotalTrackedTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalTrackedTime
        fields = ['id', 'user', 'total_time_tracked']
