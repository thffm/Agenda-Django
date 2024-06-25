from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'  #_(string) traducao
        verbose_name_plural = 'Categories'


    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


class Contact(models.Model):
    frist_name = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True) #blank = true nao obrigratorio
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True,upload_to='pictures/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 blank=True,null=True )
    
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,
                              null=True)


    def __str__(self):
        return f'{self.frist_name} {self.last}'
