from django.db import models

# Create your models here.
class Ebook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='ebooks/')
    thumbnail = models.ImageField(upload_to='thumbnails/')
    description = models.TextField()

    def __str__(self):
        return self.title