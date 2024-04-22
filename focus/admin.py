from django.contrib import admin
from .models import Achievement, FocusSession, Friend, UserAchievement, TotalTrackedTime

admin.site.register(Achievement)
admin.site.register(FocusSession)
admin.site.register(Friend)
admin.site.register(UserAchievement)
admin.site.register(TotalTrackedTime)

