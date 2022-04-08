from django.shortcuts import render
from News.models import News

# Create your views here.

def news(request):
    data = News.objects.all()
    return render(request,'News/index.html',{'data':data})

def post(request,inum):
    data = News.objects.get(id=inum)
    return render(request,'News/post.html',{'news':data})