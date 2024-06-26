from django.db import models


# Create your models here.


class Photo(models.Model):
    STATUS_CHOICES = (("published", "published"),
                      ("banned", "banned"),
                      ("pending", "pending")
                      )

    title = models.CharField(max_length=255)
    opis = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="pending")
    img = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)
    tags = models.ManyToManyField("tags.Tag", related_name="photos", blank=True)
