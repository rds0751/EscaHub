from django.contrib import admin

from .models import Blog, Tag, BlogComment
# Register your models here.

class blogAdmin(admin.ModelAdmin):
	class Meta:
		Model = Blog
		admin.site.register(Blog)

class tagAdmin(admin.ModelAdmin):
	class Meta:
		Model = Tag
		admin.site.register(Tag)

class blogCommentAdmin(admin.ModelAdmin):
	class Meta:
		Model = BlogComment
		admin.site.register(BlogComment)
