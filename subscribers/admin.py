from django.contrib import admin
from subscribers.models import * 
# Register your models here.
admin.site.register(Topic)

admin.site.register(Subscriber)
admin.site.register(Content)
