from django.contrib import admin

from .models import Category, Location, Post


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'category'
    )
    search_fields = ['title']
    list_filter = 'is_published'


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)
