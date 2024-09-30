from django.db import models
from django.contrib.auth.models import User



# class register(models.Model):
#     username = models.CharField(max_length=30, blank=True, null=True)
#     password = models.CharField(max_length=30, blank=True)
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=40, blank=False)
#     last_name = models.CharField(max_length=50, blank=False)
#
#     def __str__(self):
#         return self.email

# Create your models here.

class client(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_projects')