from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        exclude = ('bookmark_count', 'rating_score')
