from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request): 
    # if the method is POST 
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
       # if the form is valid
        if form.is_valid():
          # Yes, Save
           form.save()
           return HttpResponseRedirect('/')
        
        else:
             return HttpResponseRedirect('form.error.as_json()')

    #get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    form=PostForm

    #show
    return render(request, 'posts.html',
                      {'posts': posts})
                      
def delete(request, post_id):
  #find post
  post = Post.objects.get(id = post_id)
  post.delete()
  return HttpResponseRedirect('/')

def edit(request, post_id):
  post=Post.objects.get(id=post_id)
  if request.method == 'POST':
    form=PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
    else:
      return HttpResponseRedirect(form.errors.as_json())
  return render(request, "edit.html", {"post":post})

def like(request, post_id):
  post = Post.objects.get(id= post_id)
  new_like = post.likes+1
  post.likes = new_like
  post.save()
  return HttpResponseRedirect('/')