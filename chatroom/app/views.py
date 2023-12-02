from django.shortcuts import render

# Create your views here.
def home(request, group_name):
    return render(request, 'app/index.html', {'groupName':group_name})