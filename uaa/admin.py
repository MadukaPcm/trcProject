from django.contrib import admin
from django.contrib.auth.models import Permission,Group
from . models import User,Department,Profile

# Register your models here.
# admin.site.register(Group)
admin.site.register(Permission)
admin.site.register(User)
admin.site.register(Department)
admin.site.register(Profile)

