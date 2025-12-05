from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titel', 'slug','author','publish','status']
    list_filter = ['author','status','publish', 'created']
    search_fields = ['titel' , 'body']
    prepopulated_fields= {'slug': ('titel',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish' # فهم 
    ordering = ['status', 'publish'] # فهم 
 