from django.shortcuts import render
from Gallery.models import images

# Create your views here.
def gellery(request):
    data = images.objects.all()
    return render(request,'Gallery/index.html',{'data':data})