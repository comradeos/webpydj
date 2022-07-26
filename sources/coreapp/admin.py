from django.contrib import admin
from coreapp.models import Languages, Categories

# Register your models here.

class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_field = ('title', 'content')
    list_filter = ('is_published', 'time_create')

admin.site.register(Languages, LanguagesAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_field = ('name')

admin.site.register(Categories, CategoriesAdmin)