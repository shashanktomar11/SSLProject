from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(Membership)