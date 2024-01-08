from django.db import models
from .import constants
import datetime
# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100,null=True)
    role = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  


    
class Projects(models.Model):
    name = models.EmailField(max_length=100,blank=False)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, default='In Progress')
    leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.CharField(max_length=10, choices=constants.PRIORITY_CHOICES, default='Medium')

    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True)

class Task(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=50, default='To Do')

    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Team(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)  # You can customize this based on your needs, e.g., 'Developer', 'Manager', etc.
    created_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.user.username} - {self.project.name} - {self.role}"