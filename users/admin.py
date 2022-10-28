from django.contrib import admin

from .models import UserModel

# @admin.register(UserModel)
# class UserModelAdmin(admin.ModelAdmin):
#     list_display = 'username',
#     list_display_links = 'username'

admin.site.register(UserModel)