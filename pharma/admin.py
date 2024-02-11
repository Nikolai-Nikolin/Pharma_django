from django.contrib import admin
from pharma.models import UserCure, Cure

admin.site.register(Cure)
admin.site.register(UserCure)
