from django.contrib import admin
from .models import Post, Category, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'category', 'author']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
