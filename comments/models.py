from django.db import models

# Create your models here.



class Comment(models.Model):
    class Meta:
        abstract = True

    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PostComment(Comment):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
