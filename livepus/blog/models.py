from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Blog(models.Model):
    name = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to = 'media/blog/%Y/%m/')
    description = RichTextField()
    category = models.CharField(max_length = 255)
    subcategory = models.CharField(max_length = 255)
    created_date = models.DateTimeField(default = datetime.now, blank=True)