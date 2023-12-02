from django.shortcuts import render
from .models import Chat, Group

# Create your views here.
def home(request, group_name):
    group, created = Group.objects.get_or_create(name=group_name)
    chats = [] if created else group.chat_set.all()
    return render(request, 'app/index.html', {'groupName':group_name, 'chats':chats})