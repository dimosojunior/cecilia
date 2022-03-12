from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from DimosoApp.models import *


# Register your models here.

class ReportAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]



admin.site.register(Report, ReportAdmin)

