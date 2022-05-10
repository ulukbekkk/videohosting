from django.contrib import admin

from .models import Video, Category, Comment, Fav, Like


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('genre', 'slug')
    list_display_links = ('genre', )
    search_fields = ('genre', )
    prepopulated_fields = {'slug': ('genre', )}


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'prava', 'created_at', 'updated_at')
    list_filter = ('prava', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Comment)
admin.site.register(Fav)
admin.site.register(Like)
