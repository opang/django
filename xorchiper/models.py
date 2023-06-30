from django.db import models

# Create your models here.
class EnkripsiFiles(models.Model):
    document = models.CharField(max_length=255, blank=True)
    fi = models.FileField(upload_to='', blank=True)
    encrypted_by = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    time = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.document
    
    def delete(self, *args, **kwargs):
        self.fi.delete()
        super().delete(*args, **kwargs)


class DekripsiFiles(models.Model):
    document = models.CharField(max_length=255, blank=True)
    fi = models.FileField(upload_to='', blank=True)
    encrypted_by = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    time = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.document
    
    def delete(self, *args, **kwargs):
        self.fi.delete()
        super().delete(*args, **kwargs)