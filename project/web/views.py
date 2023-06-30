from django.shortcuts import render
# from .models import Employee
from .models import Worker

# Create your views here.
def index(request):
    #return render(request, 'web/base.html')
    nodes = Worker.objects.all()
    return render(request, "web/index.html", {'nodes': nodes}) #,   context_instance=RequestContext(request))