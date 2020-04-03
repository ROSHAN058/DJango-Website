from django.contrib import admin
from .models import Automation_tracker

# Register your models here.

from advanced_filters.admin import AdminAdvancedFiltersMixin
admin.site.site_header = "Automation Tracker Dashboard"
admin.site.index_title = "Admin"
admin.site.site_title ="Tracker"
from import_export.admin import ImportExportModelAdmin

class Auto(AdminAdvancedFiltersMixin,ImportExportModelAdmin):
    list_display = ('Team_Name', 'Automation_Status', 'Idea_Date')
    list_filter = ('Team_Name', 'Automation_Status')
    search_fields = ( 'Team_Name', 'Automation_Status', 'Idea_Date')
    advanced_filter_field = ('Team_Name', 'Automation_Status', 'Idea_Date')
    list_editables= ( 'Automation_Status', 'Idea_Date')

class ImportAdmin(admin.ModelAdmin):
 #change_list_template = 'templates/index.html'
 list_display = ('Team_Name', 'Automation_Status', 'Idea_Date')
 list_filter = ('Team_Name', 'Automation_Status')
 search_fields = ('Team_Name', 'Automation_Status', 'Idea_Date')
 advanced_filter_field = ('Team_Name', 'Automation_Status', 'Idea_Date')
 list_editable = ('Automation_Status', 'Idea_Date')


admin.site.register(Automation_tracker, ImportAdmin)

