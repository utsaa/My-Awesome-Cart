from django.shortcuts import render
from .models import Blogpost
# Create your views here.
from django.http import HttpResponse

def index(request):
    myposts=Blogpost.objects.all()
    print(myposts)
    return render(request,'blog/index.html',{'myposts': myposts})

def blogpost(request, id):
    post=Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request,'blog/blogpost.html',{'post':post})

def about(request):
    return HttpResponse('We are an about')

def search(request):
    return HttpResponse('We are an search')

def contact(request):
    return HttpResponse('We are an contact')

def productView(request):
    return HttpResponse('We are an product view')

def checkout(request):
    return HttpResponse('We are an checkout')

def tracker(request):
    return HttpResponse('We are an trackers')

