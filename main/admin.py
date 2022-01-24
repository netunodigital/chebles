from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('content', 'link_url')

@admin.register(Box1)
@admin.register(Box2)
@admin.register(Box3)
class BoxAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

@admin.register(Course1)
class Course1Admin(admin.ModelAdmin):
    list_display = ('title', 'content')
    
@admin.register(Course2)
class Course2Admin(admin.ModelAdmin):
    list_display = ('title', 'schedule')

@admin.register(Local1)
@admin.register(Local2)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('local', 'address', 'contact')
