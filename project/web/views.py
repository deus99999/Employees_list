from django.shortcuts import render
# from .models import Employee

# Create your views here.
def index(request):
    return render(request, 'web/base.html')