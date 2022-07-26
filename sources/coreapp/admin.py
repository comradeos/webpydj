from django.contrib import admin
from coreapp.models import Languages, Categories

# Register your models here.

class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_field = ('title', 'content')

admin.site.register(Languages, LanguagesAdmin)

admin.site.register(Categories)