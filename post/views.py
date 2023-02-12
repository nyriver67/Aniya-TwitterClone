from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request): 
    # if the method is POST 
    if request.method == 'POST':
        form = PostForm(request.POST)
       # if the form is valid
        if form.is_valid():
          # Yes, Save
           form.save()
           return HttpResponseRedirect('/')
        
        else:
             return HttpResponseRedirect(form.error.as_json())

    #get all posts, limit = 20
    posts = Post.objects.all()[:20]

    #show
    return render(request, 'posts.html',
                      {'posts': posts})
                      
def delete(request, post_id):
  #find post
  post = Post.objects.get(id = post_id)
  post.delete()
  return HttpResponseRedirect('/')