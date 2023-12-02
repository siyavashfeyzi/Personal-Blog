from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    short_description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Blog/images/")
    blog_text = models.TextField()
