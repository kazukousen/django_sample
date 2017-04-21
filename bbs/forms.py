from django import forms
from .models import Post, Comment

class EditorTextarea(forms.Widget):
    template_name = 'bbs/textarea.html'

    def __init__(self):
        super(EditorTextarea, self).__init__()

class PostForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(widget=EditorTextarea)

    class Meta:
        model = Post
        fields = ('title', 'description')
        exclude = ('bookmark_count', 'rating_score')
