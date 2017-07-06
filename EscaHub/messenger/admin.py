from django.contrib import admin

from .models import Message
# Register your models here.

class messageAdmin(admin.ModelAdmin):
	class Meta:
		Model = Message
		admin.site.register(Message)