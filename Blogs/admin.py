from django.contrib import admin
from .models import blog

class Admin(admin.ModelAdmin):
    list_display = ('title','published_on')
    list_filter = ("published_on",)
    search_fields = ['title', 'full_content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(blog, Admin)