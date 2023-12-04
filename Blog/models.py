from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    short_description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="image/", null=True, blank=True)
    blog_text = models.TextField()

    def get_image_url(self):
        return self.image.url

    class Meta:
        indexes = [
            models.Index(fields=["title"], name="title index"),
        ]
