from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import * 
# Register your models here.

@admin.register(City , University , Profession)
class AdminView(ImportExportModelAdmin):
    pass

# admin.site.register(City)
# admin.site.register(University)
# admin.site.register(Specialization)
# admin.site.register(Profession)