from rest_framework import generics, status
from .models import Achievement, FocusSession, Friend, UserAchievement, TotalTrackedTime
from .serializers import AchievementSerializer, FocusSessionSerializer, FriendSerializer, UserAchievementSerializer, TotalTrackedTimeSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response

from focus import serializers

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

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # Add any custom validation logic here
        # For example, check if the username is unique
        if User.objects.filter(username=serializer.validated_data['username']).exists():
            raise serializers.ValidationError("Username already exists.")
        
        # Save the new user object
        serializer.save()

    def post(self, request, *args, **kwargs):
        # Handle JSON file upload if necessary
        # For example, you might want to parse the JSON file and pass the data to the serializer
        # json_file = request.FILES.get('json_file')
        # json_data = json.loads(json_file.read())

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
