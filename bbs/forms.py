from django import forms
from .models import Post, Comment

class EditorTextarea(forms.Textarea):
    template_name = 'bbs/textarea.html'

    def __init__(self, attrs=None):
        super(EditorTextarea, self).__init__(attrs)

class PostForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(widget=EditorTextarea)

    class Meta:
        model = Post
        exclude = ('bookmark_count', 'rating_score')
