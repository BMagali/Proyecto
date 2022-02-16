from django.contrib import admin

from blog.models import Avatar, Comentario, Post, Tag

admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Tag)
admin.site.register(Avatar)