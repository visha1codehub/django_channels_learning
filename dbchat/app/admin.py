from django.contrib import admin

# Register your models here.
from .models import Chat, Group


@admin.register(Chat)
class ChatModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'time_stamp', 'group']
    
    
@admin.register(Group)
class ChatModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']