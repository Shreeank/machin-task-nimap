from django.contrib import admin
from .models import client
from .models import Project

# Register your models here.

@admin.register(client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'created_at', 'created_by']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_name', 'client', 'get_users', 'created_at', 'created_by']

    # If users is a ManyToManyField or a related field, you may need to define a method to display it
    def get_users(self, obj):
        return ", ".join([user.username for user in obj.users.all()])
    get_users.short_description = 'Users'