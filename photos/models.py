from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.


class Photo(models.Model):
    STATUS_CHOICES = (
        ("published", "published"),
        ("banned", "banned"),
        ("pending", "pending"),
    )

    title = models.CharField(max_length=255)
    opis = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="pending")
    img = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)
    tags = models.ManyToManyField("tags.Tag", related_name="photos", blank=True)

    def __str__(self):
        return self.title


    def thumbnail(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" width="100">')
        return ""

    thumbnail.shor_description = "Thumbnail"
class Gallery(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    photos = models.ManyToManyField(Photo, related_name="galleries", blank=True)

    def __str__(self):
        return self.title