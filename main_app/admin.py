from django.contrib import admin
from .models import UserProfile, Elog, Flog, User

admin.site.register(UserProfile)
#admin.site.register(Exercise)
admin.site.register(Elog)
#admin.site.register(Food)
admin.site.register(Flog)