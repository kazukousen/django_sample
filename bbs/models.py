from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from .utils import sanitize_markdown

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    bookmark_count = models.IntegerField(default=0)
    rating_score = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.description_html = sanitize_markdown(self.description)
        super(Post, self).save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse('bbs:post_detail', args=[self.id])

    def get_comments(self):
        comments = self.comment_set.all()
        return comments

class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    body_html = models.TextField(editable=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    bookmark_count = models.IntegerField(default=0)
    rating_score = models.IntegerField(default=0)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __str__(self):
        return self.body[:20]

    def save(self, *args, **kwargs):
        self.body_html = sanitize_markdown(self.body)
        super(Comment, self).save(*args, *kwargs)

    class MPTTMeta:
        order_insertion_by = ['-rating_score']
