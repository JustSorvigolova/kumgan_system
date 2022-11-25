from django.contrib import admin
from .models import Category_Transport, Box, Services, Schedule, Booking

admin.site.register(Category_Transport)
admin.site.register(Box)
admin.site.register(Schedule)
admin.site.register(Services)
admin.site.register(Booking)
