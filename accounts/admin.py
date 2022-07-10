from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# from .models import User

CustomUser = get_user_model()
# adminフォーム
# admin.site.unregister(CustomUser)
admin.site.register(CustomUser, UserAdmin)
# admin.site.register(CustomUser)
