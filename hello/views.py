from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
# Create your views here.
def home(request):
    blogs = Blog.objects
    return render (request, 'home.html', {'blogs':blogs})

def new(request):
    return render (request, 'new.html')

def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST ['title']
        post.body = request.POST ['body']
        post.save()
    return redirect ('home')

def detail(request, post_id):
    onepost = get_object_or_404(Blog, pk=post_id)
    return render (request, 'detail.html', {'onepost': onepost})


def edit(request, post_id):
    onepost = get_object_or_404(Blog, pk=post_id)
    return render (request, 'edit.html', {'onepost': onepost})

def update(request, post_id):
        updatepost = get_object_or_404(Blog, pk=post_id)
        updatepost.title = request.POST ['title']
        updatepost.body = request.POST ['body']
        updatepost.save()
        return redirect ('/detail/' + str(post_id))


def delete (request, post_id):
        deletepost = get_object_or_404(Blog, pk=post_id)
        deletepost.delete()
        return redirect ('home')


