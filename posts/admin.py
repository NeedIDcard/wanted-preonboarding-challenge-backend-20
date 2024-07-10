from django.contrib import admin
from posts.models import Post, PostImage, Comment
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('photo')
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "content",
    ]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo",
    ]

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
    ]