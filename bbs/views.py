from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Post, Comment
from .utils import object_list

def post_list(request, queryset=None, **kwargs):
    if queryset is None:
        queryset = Post.objects.all()

    return object_list(
        request,
        queryset=queryset,
        paginate_by=20,
        **kwargs
    )
