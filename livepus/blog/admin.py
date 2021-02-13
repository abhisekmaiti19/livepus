from django.contrib import admin
from .models import Blog

class blogAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_field = ('name','category')
    list_display_links = ('id','name')

admin.site.register(Blog, blogAdmin)
