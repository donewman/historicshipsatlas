from django.db import models

class Flag(models.Model):
	# Defines flags.
	flag=models.CharField(max_length=200)

	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse("flag_detail", args=[str(self.id)])

	def __str__(self):
		return self.flag

class Type(models.Model):
	# Defines types of ship.
	type=models.CharField(max_length=200)

	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse("type_detail", args=[str(self.id)])

	def __str__(self):
		return self.type

class City(models.Model):
	# Defines cities.
	city_name=models.CharField(max_length=200)
	city_region=models.CharField(max_length=200, blank=True)

	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse("city_detail", args=[str(self.id)])

	def __str__(self):
		if self.city_region:
			return "%s, %s" % (self.city_name, self.city_region)
		else:
			return self.city_name

class Country(models.Model):
	# Defines countries.
	country=models.CharField(max_length=200)

	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse("country_detail", args=[str(self.id)])

	def __str__(self):
		return self.country

class Builder(models.Model):
	# Defines builders.
	builder_name=models.CharField(max_length=200)
	builder_city=models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
	builder_country=models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse("builder_detail", args=[str(self.id)])

	def __str__(self):
		return "%s, %s, %s" % (self.builder_name, self.builder_city, self.builder_country)

class Register(models.Model):
	# Defines historic registers.
	register=models.CharField(max_length=200)

	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse("register_detail", args=[str(self.id)])

	def __str__(self):
		return self.register

class Use(models.Model):
	# Defines uses.
	use=models.CharField(max_length=200)

	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse("use_detail", args=[str(self.id)])

	def __str__(self):
		return self.use

class Status(models.Model):
	# Defines statuses.
	status=models.CharField(max_length=200)

	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse("status_detail", args=[str(self.id)])

	def __str__(self):
		return self.status

class Owner(models.Model):
	# Defines owners.
	owner=models.CharField("Name of Owner", max_length=200)

	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse("owner_detail", args=[str(self.id)])

	def __str__(self):
		return self.owner

class Ship(models.Model):
	# Defines each ship in the database.
	name=models.CharField("Name", max_length=200)
	imo=models.PositiveIntegerField("IMO Number", null=True, blank=True)
	type=models.ForeignKey(Type, on_delete=models.SET_NULL, verbose_name="Type of Ship", null=True)
	year_built=models.PositiveSmallIntegerField("Year Built")
	builder=models.ForeignKey(Builder, on_delete=models.SET_NULL, verbose_name="Builder", null=True, blank=True)
	tonnage=models.PositiveIntegerField("Gross Tonnage", null=True, blank=True)
	length=models.FloatField("Length (m)", null=True, blank=True)
	beam=models.FloatField("Beam (m)", null=True, blank=True)
	city=models.ForeignKey(City, on_delete=models.SET_NULL, verbose_name="Location - City", null=True, blank=True)
	country=models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name="Location - Country", null=True, blank=True)
	registers=models.ManyToManyField(Register, verbose_name="Historic Register(s)", blank=True)
	status=models.ForeignKey(Status, on_delete=models.SET_NULL, verbose_name="Current Status", null=True)
	uses=models.ManyToManyField(Use, verbose_name="Current Use(s)", blank=True)
	flag=models.ForeignKey(Flag, on_delete=models.SET_NULL, verbose_name="Flag", null=True, blank=True)
	owner=models.ForeignKey(Owner, on_delete=models.SET_NULL, verbose_name="Owner", null=True, blank=True)
	website=models.URLField("Website", blank=True)
	former_names=models.TextField("Former Names", blank=True)
	description=models.TextField("Description", blank=True)
	lat=models.FloatField("Latitude", null=True, blank=True)
	lon=models.FloatField("Longitude", null=True, blank=True)

	def get_absolute_url(self):
	    from django.urls import reverse
	    return reverse("ship_detail", args=[str(self.id)])

	def __str__(self):
		return self.name
