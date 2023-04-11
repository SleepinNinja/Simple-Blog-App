from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    posts = models.Post.objects.all()
    return render(request, 'index.html', {'posts': posts})



def post(request, id):
    post = models.Post.objects.get(id = id)
    return render(request, 'post.html', {'post': post})
