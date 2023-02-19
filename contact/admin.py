from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'created_date']
    date_hierarchy = 'created_date'
    search_fields = ['name', 'phone', 'email']


admin.site.register(Contact, ContactAdmin)
