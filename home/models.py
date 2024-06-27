from django.db import models

# Create your models here.


class UserInquiry(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} {self.email} {self.created_at}"
