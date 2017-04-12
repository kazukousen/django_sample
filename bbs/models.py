from django.db import models

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

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', blank=True, null=True)
    body = models.TextField()
    body_html = models.TextField(editable=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    bookmark_count = models.IntegerField(default=0)
    rating_score = models.IntegerField(default=0)

    def __str__(self):
        return self.body[:20]
