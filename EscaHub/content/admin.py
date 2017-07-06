from django.contrib import admin

# Register your models here.
from .models import Trip, TripImage, Variation, TripItinerary, ItineraryDay

class TripAdmin(admin.ModelAdmin):
	date_hierarchy = 'timestamp' #updated
	search_fields = ['title', 'highlights']
	list_display = ['title', 'price', 'active', 'updated']
	list_editable = ['price', 'active']
	list_filter = ['price', 'active']
	readonly_fields = ['updated', 'timestamp']
	prepopulated_fields = {"slug": ("title",)}
	class Meta:
		model = Trip

admin.site.register(Trip, TripAdmin)
admin.site.register(ItineraryDay)
admin.site.register(TripItinerary)
admin.site.register(TripImage)
admin.site.register(Variation)