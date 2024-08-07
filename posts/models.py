from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="User",
        on_delete=models.CASCADE,
    )
    content = models.TextField("content")
    created = models.DateTimeField("created_time", auto_now_add=True)

class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name="Post",
        on_delete=models.CASCADE,
    )
    photo = models.ImageField("photo",upload_to="post")

class Comment(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="User",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
    content = models.TextField("content")
    created = models.DateTimeField("created_time", auto_now_add=True)