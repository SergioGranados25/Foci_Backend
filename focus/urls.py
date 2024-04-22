from django.urls import path
from .views import (
    AchievementList, AchievementCreate, AchievementRetrieve,
    AchievementUpdate, AchievementDestroy,
    FocusSessionList, FocusSessionCreate, FocusSessionRetrieve,
    FocusSessionUpdate, FocusSessionDestroy,
    FriendList, FriendCreate, FriendRetrieve,
    FriendUpdate, FriendDestroy,
    UserAchievementList, UserAchievementCreate,
    UserAchievementRetrieve, UserAchievementUpdate,
    UserAchievementDestroy,TotalTrackedTimeListCreateAPIView, 
    TotalTrackedTimeRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Achievements
    path('achievements/', AchievementList.as_view(), name='achievement-list'),
    path('achievements/create/', AchievementCreate.as_view(), name='achievement-create'),
    path('achievements/<int:pk>/', AchievementRetrieve.as_view(), name='achievement-retrieve'),
    path('achievements/<int:pk>/update/', AchievementUpdate.as_view(), name='achievement-update'),
    path('achievements/<int:pk>/delete/', AchievementDestroy.as_view(), name='achievement-destroy'),

    # Focus Sessions
    path('focus-sessions/', FocusSessionList.as_view(), name='focus-session-list'),
    path('focus-sessions/create/', FocusSessionCreate.as_view(), name='focus-session-create'),
    path('focus-sessions/<int:pk>/', FocusSessionRetrieve.as_view(), name='focus-session-retrieve'),
    path('focus-sessions/<int:pk>/update/', FocusSessionUpdate.as_view(), name='focus-session-update'),
    path('focus-sessions/<int:pk>/delete/', FocusSessionDestroy.as_view(), name='focus-session-destroy'),

    # Friends
    path('friends/', FriendList.as_view(), name='friend-list'),
    path('friends/create/', FriendCreate.as_view(), name='friend-create'),
    path('friends/<int:pk>/', FriendRetrieve.as_view(), name='friend-retrieve'),
    path('friends/<int:pk>/update/', FriendUpdate.as_view(), name='friend-update'),
    path('friends/<int:pk>/delete/', FriendDestroy.as_view(), name='friend-destroy'),

    # User Achievements
    path('user-achievements/', UserAchievementList.as_view(), name='user-achievement-list'),
    path('user-achievements/create/', UserAchievementCreate.as_view(), name='user-achievement-create'),
    path('user-achievements/<int:pk>/', UserAchievementRetrieve.as_view(), name='user-achievement-retrieve'),
    path('user-achievements/<int:pk>/update/', UserAchievementUpdate.as_view(), name='user-achievement-update'),
    path('user-achievements/<int:pk>/delete/', UserAchievementDestroy.as_view(), name='user-achievement-destroy'),

    # Total Tracked Time
    path('total-tracked-time/', TotalTrackedTimeListCreateAPIView.as_view(), name='total-tracked-time-list-create'),
    path('total-tracked-time/<int:pk>/', TotalTrackedTimeRetrieveUpdateDestroyAPIView.as_view(), name='total-tracked-time-detail'),
]
