from django.contrib import admin

from webapp.models import Book


class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'email', 'text', 'CreatedDate', 'LastEditDate', 'status']
    list_filter = ['status']
    list_display_links = ['pk', 'author']
    search_fields = ['status']
    fields = ['author', 'email', 'text', 'status']


admin.site.register(Book, TaskAdmin)