from rest_framework import generics
from .models import Achievement, FocusSession, Friend, UserAchievement, TotalTrackedTime
from .serializers import AchievementSerializer, FocusSessionSerializer, FriendSerializer, UserAchievementSerializer, TotalTrackedTimeSerializer

class AchievementList(generics.ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class AchievementCreate(generics.CreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class AchievementRetrieve(generics.RetrieveAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class AchievementUpdate(generics.UpdateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class AchievementDestroy(generics.DestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class FocusSessionList(generics.ListAPIView):
    queryset = FocusSession.objects.all()
    serializer_class = FocusSessionSerializer

class FocusSessionCreate(generics.CreateAPIView):
    queryset = FocusSession.objects.all()
    serializer_class = FocusSessionSerializer

class FocusSessionRetrieve(generics.RetrieveAPIView):
    queryset = FocusSession.objects.all()
    serializer_class = FocusSessionSerializer

class FocusSessionUpdate(generics.UpdateAPIView):
    queryset = FocusSession.objects.all()
    serializer_class = FocusSessionSerializer

class FocusSessionDestroy(generics.DestroyAPIView):
    queryset = FocusSession.objects.all()
    serializer_class = FocusSessionSerializer

class FriendList(generics.ListAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class FriendCreate(generics.CreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class FriendRetrieve(generics.RetrieveAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class FriendUpdate(generics.UpdateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class FriendDestroy(generics.DestroyAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class UserAchievementList(generics.ListAPIView):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer

class UserAchievementCreate(generics.CreateAPIView):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer

class UserAchievementRetrieve(generics.RetrieveAPIView):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer

class UserAchievementUpdate(generics.UpdateAPIView):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer

class UserAchievementDestroy(generics.DestroyAPIView):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer

class TotalTrackedTimeListCreateAPIView(generics.ListCreateAPIView):
    queryset = TotalTrackedTime.objects.all()
    serializer_class = TotalTrackedTimeSerializer

class TotalTrackedTimeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TotalTrackedTime.objects.all()
    serializer_class = TotalTrackedTimeSerializer