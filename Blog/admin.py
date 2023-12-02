from django.contrib import admin
from . import models
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Post, BlogAdmin)
