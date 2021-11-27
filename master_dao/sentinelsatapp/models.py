from django.db import models

# Create your models here.
class Properties(models.Model):
	properties_id = models.AutoField(primary_key=True)
	datatakesensingstart = models.CharField(max_length=100)
	orbitnumber = models.IntegerField()
	hv_order_tileid = models.CharField(max_length=100)
	cloudcoverpercentage = models.CharField(max_length=100)
	link = models.CharField(max_length=100)
	orbitdirection = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	uuid = models.CharField(max_length=100)
	beginposition = models.CharField(max_length=100)
	producttype = models.CharField(max_length=100)
	endposition = models.CharField(max_length=100)
	relativeorbitnumber = models.CharField(max_length=100)
	level1cpdiidentifier = models.CharField(max_length=100)
	processingbaseline = models.CharField(max_length=100)
	id = models.CharField(max_length=100)
	instrumentname = models.CharField(max_length=100)
	ondemand = models.BooleanField()
	summary = models.CharField(max_length=100)
	identifier = models.CharField(max_length=100)
	instrumentshortname = models.CharField(max_length=100)
	link_alternative = models.CharField(max_length=100)
	sensoroperationalmode = models.CharField(max_length=100)
	tileid = models.CharField(max_length=100)
	format = models.CharField(max_length=100)
	granuleidentifier = models.CharField(max_length=100)
	platformname = models.CharField(max_length=100)
	filename = models.CharField(max_length=100)
	link_icon = models.CharField(max_length=100)
	size = models.CharField(max_length=100)
	datastripidentifier = models.CharField(max_length=100)
	platformserialidentifier = models.CharField(max_length=100)
	ingestiondate = models.CharField(max_length=100)
	processinglevel = models.CharField(max_length=100)
	platformidentifier = models.CharField(max_length=100)
	s2datatakeid = models.CharField(max_length=100)
	