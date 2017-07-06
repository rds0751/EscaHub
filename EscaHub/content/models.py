from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
# Create your models here.


# Goa 1
# Kasol Narkanda 2
# Rishikesh 3


class Trip(models.Model):
	title = models.CharField(max_length=120)
	highlights = models.TextField(null=True, blank=True)
	terms = models.TextField(null=True, blank=True)
	policy = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	sale_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
	costing_includes = models.TextField(null=True, blank=True)
	costing_excludes = models.TextField(null=True, blank=True)
	departure_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
	arrival_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)
	update_defaults = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title

	class Meta:
		unique_together = ('title', 'slug')

	def get_price(self):
		return self.price

	def get_absolute_url(self):
		return reverse("single_trip", kwargs={"slug": self.slug})


class TripImage(models.Model):
	title = models.CharField(max_length=120, null=True)
	trip = models.ForeignKey(Trip)
	image = models.ImageField(upload_to='trips/images/')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)



class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)

	def duration(self):
		return self.all().filter(category='duration')

	def month(self):
		return self.all().filter(category='month')


VAR_CATEGORIES = (
	('duration', 'duration'),
	('month', 'month'),
	('price', 'price'),
	)


class Variation(models.Model):
	trip = models.ForeignKey(Trip)
	category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='duration')
	title = models.CharField(max_length=120)
	image = models.ForeignKey(TripImage, null=True, blank=True)
	price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)
	objects = VariationManager()

	def __unicode__(self):
		return self.title

class TripItinerary(models.Model):
	trip = models.ForeignKey(Trip)
	day = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

	class Meta:
		unique_together = ('trip', 'day')

class ItineraryDay(models.Model):
	tripItinerary = models.ForeignKey(TripItinerary, null=True, blank=True)
	title = models.CharField(max_length=120, null=True, blank=True)
	slot1 = models.CharField(max_length=300, null=True, blank=True)
	slot2 = models.CharField(max_length=300, null=True, blank=True)
	slot3 = models.CharField(max_length=300, null=True, blank=True)
	slot4 = models.CharField(max_length=300, null=True, blank=True)
	slot5 = models.CharField(max_length=300, null=True, blank=True)
	slot6 = models.CharField(max_length=300, null=True, blank=True)
	slot7 = models.CharField(max_length=300, null=True, blank=True)
	slot8 = models.CharField(max_length=300, null=True, blank=True)
	slot9 = models.CharField(max_length=300, null=True, blank=True)
	slot10 = models.CharField(max_length=300, null=True, blank=True)
	slot11 = models.CharField(max_length=300, null=True, blank=True)
	slot12 = models.CharField(max_length=300, null=True, blank=True)
	slot13 = models.CharField(max_length=300, null=True, blank=True)
	slot14 = models.CharField(max_length=300, null=True, blank=True)
	slot15 = models.CharField(max_length=300, null=True, blank=True)
	slot16 = models.CharField(max_length=300, null=True, blank=True)
	slot17 = models.CharField(max_length=300, null=True, blank=True)
	slot18 = models.CharField(max_length=300, null=True, blank=True)
	slot18 = models.CharField(max_length=300, null=True, blank=True)
	slot20 = models.CharField(max_length=300, null=True, blank=True)



def trip_defaults(sender, instance, created, *args, **kwargs):
	if instance.update_defaults:
		categories = instance.category.all()
		print (categories)
		for cat in categories:
			print (cat.id)
			if cat.id == 1: #for t-shirts
				small_duration = Variation.objects.get_or_create(trip=instance, 
											category='duration', 
											title='Small')
				medium_duration = Variation.objects.get_or_create(trip=instance, 
											category='duration', 
											title='Medium')
				long_duration = Variation.objects.get_or_create(trip=instance, 
											category='duration', 
											title='Long')
		instance.update_defaults = False
		instance.save()
	#print args, kwargs

post_save.connect(trip_defaults, sender=Trip)