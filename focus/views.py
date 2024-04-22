from rest_framework import generics
from .models import Achievement, FocusSession, Friend, UserAchievement, TotalTrackedTime
from .serializers import AchievementSerializer, FocusSessionSerializer, FriendSerializer, UserAchievementSerializer, TotalTrackedTimeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class AchievementList(generics.ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    http_method_names = ['get']

class AchievementCreate(generics.CreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    http_method_names = ['post']

class AchievementRetrieve(generics.RetrieveAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    http_method_names = ['get']

class AchievementUpdate(generics.UpdateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    http_method_names = ['put']

class AchievementDestroy(generics.DestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    http_method_names = ['delete']

class FocusSessionList(generics.ListAPIView):
    queryset = FocusSession.objects.all()
    serializer_class = FocusSessionSerializer
    http_method_names = ['get']

class FocusSessionCreate(generics.CreateAPIView):
    queryset = FocusSession.objects.all()
    serializer_class = FocusSessionSerializer
    http_method_names = ['post']

class FocusSessionRetrieve(generics.RetrieveAPIView):
    queryset = FocusSession.objects.all()
    serializer_class = FocusSessionSerializer
    http_method_names = ['get']

class FocusSessionUpdate(generics.UpdateAPIView):
    queryset = FocusSession.objects.all()
    serializer_class = FocusSessionSerializer
    http_method_names = ['put']

class FocusSessionDestroy(generics.DestroyAPIView):
    queryset = FocusSession.objects.all()
    serializer_class = FocusSessionSerializer
    http_method_names = ['delete']

class FriendList(generics.ListAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    http_method_names = ['get']

class FriendCreate(generics.CreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    http_method_names = ['post']

class FriendRetrieve(generics.RetrieveAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    http_method_names = ['get']

class FriendUpdate(generics.UpdateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    http_method_names = ['put']

class FriendDestroy(generics.DestroyAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    http_method_names = ['delete']

class UserAchievementList(generics.ListAPIView):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer
    http_method_names = ['get']

class UserAchievementCreate(generics.CreateAPIView):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer
    http_method_names = ['post']

class UserAchievementRetrieve(generics.RetrieveAPIView):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer
    http_method_names = ['get']

class UserAchievementUpdate(generics.UpdateAPIView):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer
    http_method_names = ['put']

class UserAchievementDestroy(generics.DestroyAPIView):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer
    http_method_names = ['delete']

class TotalTrackedTimeListAPIView(generics.ListAPIView):
    queryset = TotalTrackedTime.objects.all()
    serializer_class = TotalTrackedTimeSerializer
    http_method_names = ['get']


class TotalTrackedTimeCreateAPIView(generics.CreateAPIView):
    queryset = TotalTrackedTime.objects.all()
    serializer_class = TotalTrackedTimeSerializer
    http_method_names = ['post']


class TotalTrackedTimeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = TotalTrackedTime.objects.all()
    serializer_class = TotalTrackedTimeSerializer
    http_method_names = ['get']


class TotalTrackedTimeUpdateAPIView(generics.UpdateAPIView):
    queryset = TotalTrackedTime.objects.all()
    serializer_class = TotalTrackedTimeSerializer
    http_method_names = ['put']


class TotalTrackedTimeDestroyAPIView(generics.DestroyAPIView):
    queryset = TotalTrackedTime.objects.all()
    serializer_class = TotalTrackedTimeSerializer
    http_method_names = ['delete']
