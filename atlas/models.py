"""
Models for atlas app in historicshipsatlas project.
"""

from django.db import models

# Define types of ship
class Type(models.Model):
	name = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, null=True, db_index=True)

	def __str__(self):
		return self.name

	# Get natural key for serialization
	def natural_key(self):
		return self.name

	# Get URL for details page
	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse('type_detail', args=[self.slug])

# Define cities
class City(models.Model):
	name = models.CharField(max_length=200)
	region = models.CharField(max_length=200, blank=True)
	slug = models.SlugField(max_length=200, null=True, db_index=True)

	# Ensure 'name, region' (where applicable) is unique for natural key
	class Meta:
		unique_together = ('name', 'region')

	# Return 'name, region' if region is present, otherwise just name
	def __str__(self):
		if self.region:
			return '%s, %s' % (self.name, self.region)
		else:
			return self.name

	# Get natural key for serialization--'name, region' if region is present, otherwise just name
	def natural_key(self):
		if self.region:
			return '%s, %s' % (self.name, self.region)
		else:
			return self.name

	# Get URL for details page
	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse('city_detail', args=[self.slug])

# Define countries
class Country(models.Model):
	name = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, null=True, db_index=True)

	def __str__(self):
		return self.name

	# Get natural key for serialization
	def natural_key(self):
		return self.name

	# Get URL for details page
	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse('country_detail', args=[self.slug])

# Define builders
class Builder(models.Model):
	name = models.CharField(max_length=200)
	city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
	slug = models.SlugField(max_length=200, null=True, db_index=True)

	# Ensure 'name, city, country' is unique for natural key
	class Meta:
		unique_together = ('name', 'city', 'country')

	def __str__(self):
		return '%s, %s, %s' % (self.name, self.city, self.country)

	# Get natural key for serialization
	def natural_key(self):
		return '%s, %s, %s' % (self.name, self.city, self.country)

	# Get URL for details page
	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse('builder_detail', args=[self.slug])

# Define historic registers
class Register(models.Model):
	name = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, null=True, db_index=True)

	def __str__(self):
		return self.name

	# Get natural key for serialization
	def natural_key(self):
		return self.name

	# Get URL for details page
	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse('register_detail', args=[self.slug])

# Define statuses
class Status(models.Model):
	name = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, null=True, db_index=True)

	def __str__(self):
		return self.name

	# Get natural key for serialization
	def natural_key(self):
		return self.name

	# Get URL for details page
	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse('status_detail', args=[self.slug])

# Define uses
class Use(models.Model):
	name = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, null=True, db_index=True)

	def __str__(self):
		return self.name

	# Get natural key for serialization
	def natural_key(self):
		return self.name

	# Get URL for details page
	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse('use_detail', args=[self.slug])

# Define owners
class Owner(models.Model):
	name = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, null=True, db_index=True)

	def __str__(self):
		return self.name

	# Get natural key for serialization
	def natural_key(self):
		return self.name

	# Get URL for details page
	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse('owner_detail', args=[self.slug])

# Define each ship in the database
# All other models are referenced by the Ship model
class Ship(models.Model):
	name=models.CharField('Name', max_length=200)
	imo=models.PositiveIntegerField('IMO Number', null=True, blank=True)
	fleetmon=models.PositiveIntegerField('FleetMon ID', null=True, blank=True)
	type=models.ForeignKey(Type, on_delete=models.SET_NULL, verbose_name='Type of Ship', null=True)
	year_built=models.PositiveSmallIntegerField('Year Built')
	builder=models.ForeignKey(Builder, on_delete=models.SET_NULL, verbose_name='Builder', null=True, blank=True)
	tonnage=models.PositiveIntegerField('Gross Tonnage', null=True, blank=True)
	length=models.FloatField('Length (m)', null=True, blank=True)
	beam=models.FloatField('Beam (m)', null=True, blank=True)
	city=models.ForeignKey(City, on_delete=models.SET_NULL, verbose_name='Location - City', null=True, blank=True)
	country=models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name='Location - Country', null=True, blank=True)
	registers=models.ManyToManyField(Register, verbose_name='Historic Register(s)', blank=True)
	status=models.ForeignKey(Status, on_delete=models.SET_NULL, verbose_name='Current Status', null=True)
	uses=models.ManyToManyField(Use, verbose_name='Current Use(s)', blank=True)
	owner=models.ForeignKey(Owner, on_delete=models.SET_NULL, verbose_name='Owner', null=True, blank=True)
	website=models.URLField('Website', blank=True)
	former_names=models.TextField('Former Names', blank=True)
	description=models.TextField('Description', blank=True)
	lat=models.FloatField('Latitude', null=True, blank=True)
	lon=models.FloatField('Longitude', null=True, blank=True)
	slug=models.SlugField('Slug', max_length=205, null=True, db_index=True)

	def __str__(self):
		return self.name

	# Get URL for details page
	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse('ship_detail', args=[self.slug])
