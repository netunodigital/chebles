from distutils.text_file import TextFile
from django.db import models
from pygments import highlight
from django.utils.translation import ugettext_lazy as _


class Home(models.Model):
    title = models.CharField(max_length=200, blank=False)
    subtitle = models.TextField(max_length = 200, blank=False)
    button_text = models.CharField(max_length=20, blank=False)
    button_url = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='images')
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('Home')
        verbose_name_plural = _('Home')


class About(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(max_length = 2000, blank=False)
    image = models.ImageField(upload_to='images')
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('About')
        verbose_name_plural = _('About')


class Banner(models.Model):
    content = models.CharField(max_length=500, blank=False)
    link_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Banner')


class Box1(models.Model):
    title = models.CharField(max_length=30, blank=False)
    content = models.TextField(max_length = 200, blank=False)
    button_text = models.CharField(max_length=20, blank=False)
    button_url = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='images')
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('Box 1')
        verbose_name_plural = _('Box 1')
        

class Box2(models.Model):
    title = models.CharField(max_length=30, blank=False)
    content = models.TextField(max_length = 200, blank=False)
    button_text = models.CharField(max_length=20, blank=False)
    button_url = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='images')
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('Box 2')
        verbose_name_plural = _('Box 2')
        

class Box3(models.Model):
    title = models.CharField(max_length=30, blank=False)
    content = models.TextField(max_length = 200, blank=False)
    image = models.ImageField(upload_to='images')
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('Box 3')
        verbose_name_plural = _('Box 3')
        

class Course1(models.Model):
    title = models.CharField(max_length=30, blank=False)
    content = models.TextField(max_length = 200, blank=False)
    highlight = models.TextField(max_length = 200, blank=False)
    button_text = models.CharField(max_length=20, blank=False)
    button_url = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='images')
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('Course 1')
        verbose_name_plural = _('Course 1')
        
    
class Course2(models.Model):
    title = models.CharField(max_length=30, blank=False)
    schedule = models.TextField(max_length = 200, blank=False)
    button_text = models.CharField(max_length=20, blank=False)
    button_url = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='images')
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('Course 2')
        verbose_name_plural = _('Course 2')
        

class Local1(models.Model):
    local = models.CharField(max_length=30, blank=False)
    address = models.TextField(max_length = 200, blank=False)
    contact = models.CharField(max_length = 200, blank=False)
    map_url = models.URLField(blank=False)
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('Local 1')
        verbose_name_plural = _('Local 1')
        

class Local2(models.Model):
    local = models.CharField(max_length=30, blank=False)
    address = models.TextField(max_length = 200, blank=False)
    contact = models.CharField(max_length = 200, blank=False)
    map_url = models.URLField(blank=False)
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('Local 2')
        verbose_name_plural = _('Local 2')
        

