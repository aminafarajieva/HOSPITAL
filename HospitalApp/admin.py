from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Hospital)
admin.site.register(MainDoctor)
admin.site.register(Doctor)
admin.site.register(Nurses)
admin.site.register(Patients)