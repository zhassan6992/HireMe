from django.contrib import admin
from .models import Job,HiringRequest,AcceptedRequest
# Register your models here.

admin.site.register(Job)
admin.site.register(HiringRequest)
admin.site.register(AcceptedRequest)
