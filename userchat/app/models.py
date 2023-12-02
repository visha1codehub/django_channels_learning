from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    time_stamp = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.content