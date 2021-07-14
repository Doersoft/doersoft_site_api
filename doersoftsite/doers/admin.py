from django.contrib import admin

from .models import BaseUser

# admin.site.register(BaseUserManager)
admin.site.register(BaseUser)