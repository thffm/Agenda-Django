from django.db import models
from django.utils import timezone

class Contact(models.Model):
    frist_name = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True) #blank = true nao obrigratorio
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
