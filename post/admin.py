from django.contrib import admin
from .models import Post, Genre, Type, Comment, Pub


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'realisateur', 'type', 'picture', 'video', 'date']
    search_field = ['Question_text']
    list_filter = ('author', 'type', 'genre', 'date')


admin.site.register(Post, PostAdmin)
admin.site.register(Genre)
admin.site.register(Type)
admin.site.register(Comment)
admin.site.register(Pub)