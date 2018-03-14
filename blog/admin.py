from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text','count_text']
    list_display_links = ['title']

    def count_text(self,post):
        return '{}글자'.format(len(post.text))
    count_text.short_description = "내용의 글자수"

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)