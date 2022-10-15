from django.contrib import admin
from first_app.models import Topic, Webpage, AccessRecord, UserM, UserProfileInfo

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(UserM)
admin.site.register(UserProfileInfo)
