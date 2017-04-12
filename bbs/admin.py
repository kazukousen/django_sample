from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
