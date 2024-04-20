from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Achievement, FocusSession, Friend, UserAchievement

admin.site.register(Achievement)
admin.site.register(FocusSession)
admin.site.register(Friend)
admin.site.register(UserAchievement)