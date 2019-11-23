from django.contrib import admin

from .models import Profile
from .models import Friend
from .models import Group
from .models import Membership

# Register your models here.

admin.site.register(Profile)
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(Membership)
