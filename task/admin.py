from django.contrib import admin

from .models import Category, DailyTask

# Register your models here.
admin.site.register(Category)
admin.site.register(DailyTask)
