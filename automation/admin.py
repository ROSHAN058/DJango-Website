from django.contrib import admin
from .models import Automation,AICC

# Register your models here.


admin.site.site_header = "Automation Tracker Dashboard"

admin.site.site_title ="Tracker"
from import_export.admin import ImportExportModelAdmin
from advanced_filters.admin import AdminAdvancedFiltersMixin
search_fields = ( )
class Auto(AdminAdvancedFiltersMixin,ImportExportModelAdmin):
    list_display = ('Team_Name', 'Automation_Status', 'Idea_Date')
    list_filter = ('Team_Name', 'Automation_Status')
    search_fields = ( 'Team_Name', 'Automation_Status', 'Idea_Date')
    advanced_filter_field = ('Team_Name', 'Automation_Status', 'Idea_Date')
    list_editables = ('Automation_Status', 'Idea_Date')

class ImportAdmin(admin.ModelAdmin):
    change_list_template = 'templates/index.html'
    list_display = ('Team_Name', 'Automation_Status', 'Idea_Date')
    list_filter = ('Team_Name', 'Automation_Status')
    search_fields = ('Team_Name', 'Automation_Status', 'Idea_Date')
    advanced_filter_field = ('Team_Name', 'Automation_Status', 'Idea_Date')
    list_editable = ('Automation_Status', 'Idea_Date')


admin.site.register(Automation, Auto)
from django.contrib.admin import AdminSite
class EventAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"

event_admin_site = EventAdminSite(name='event_admin')

from django.contrib.auth.models import User, Group
event_admin_site.register(AICC,Auto)
event_admin_site.register(User)
event_admin_site.register(Group)