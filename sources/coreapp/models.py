from django.db import models
from django.urls import reverse

# Create your models here.
class Languages(models.Model):
    title = models.CharField(max_length=255)
    # title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='images/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    class Meta:
        verbose_name = 'Language' # відображення в адмін панелі
        verbose_name_plural = 'Languages' # відображення у множині
        ordering = ['time_create', 'title'] # сортування в адмін панелі та на сайті


class Categories(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        