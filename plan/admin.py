from django.contrib import admin

from .models import Profession, Lernfeld, Lerneinheit, Thema

# Register your models here.

admin.site.register(Profession)
admin.site.register(Thema)

# admin.site.register(Lernfeld)

@admin.register(Lernfeld)
class LernfeldAdmin(admin.ModelAdmin):
    list_display = ['nummer', 'prof_abb', 'designation', 'content', 'time']
    list_filter = ['profession']
    @admin.display()
    def prof_abb(self, obj):
        return obj.profession.abbreviation
    def time(self, obj):
        return obj.time1 + obj.time2 + obj.time3

    search_fields = ['designation', 'content']

@admin.register(Lerneinheit)
class LerneinheitAdmin(admin.ModelAdmin):
        filter_horizontal = ['lernfeld']