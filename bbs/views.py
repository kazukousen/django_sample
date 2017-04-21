from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Post, Comment
from .forms import PostForm
from .utils import object_list, object_detail

def post_list(request, queryset=None, **kwargs):
    if queryset is None:
        queryset = Post.objects.all()

    return object_list(
        request,
        queryset=queryset,
        paginate_by=20,
        **kwargs
    )

def post_detail(request, post_id):
    return object_detail(
        request,
        queryset=Post.objects.all(),
        object_id=post_id,
    )

def edit_post(request, post_id=None, template_name='bbs/edit_post.html'):
    if post_id:
        post = get_object_or_404(Post, pk=post_id)
    else:
        template_name = 'bbs/add_post.html'
        post = Post()

    if request.method=='POST':
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            post = form.save()
            messages.info(request, 'Your post has been saved')
            return redirect(post)
    else:
        form = PostForm(instance=post)

    return render(request, template_name, {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('bbs:post_list')
