from django.db import models
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('bbs:post_detail', args=[self.id])

    def get_comments(self):
        comments = self.comment_set.order_by('path')
        return comments

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    path = models.TextField(null=False, default='')
    body = models.TextField()
    body_html = models.TextField(editable=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    bookmark_count = models.IntegerField(default=0)
    rating_score = models.IntegerField(default=0)
    path_depth = models.PositiveIntegerField(editable=False, default=1)

    def __str__(self):
        return self.body[:20]

    def save(self, *args, **kwargs):
        self.path_depth = len(self.path) - len(self.path.replace('/', '')) - 1
        return super(Comment, self).save(*args, **kwargs)

    def path_depth_range(self):
        return range(1, self.path_depth)
