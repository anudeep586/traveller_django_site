from .models import Destination
from django.shortcuts import render

# Create your views here.
def index(request):
  
    
    
    if 'q' in request.GET:
        q=request.GET['q']
        dests=Destination.objects.filter(name__icontains=q)
    else:
        dests=Destination.objects.all()

    return render(request,'index.html',{'dests':dests})
def citypune(request):
    
    dests=Pune.objects.all()



    return render(request,'citypune.html',{'dests':dests})

