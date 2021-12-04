from django.db import models

# Create your models here.
class Propertie(models.Model):

    datatakesensingstart = models.CharField(max_length=255)
    orbitnumber = models.IntegerField()
    hv_order_tileid = models.CharField(max_length=255)
    cloudcoverpercentage = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    orbitdirection = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    beginposition = models.CharField(max_length=255)
    producttype = models.CharField(max_length=255)
    endposition = models.CharField(max_length=255)
    relativeorbitnumber = models.CharField(max_length=255)
    level1cpdiidentifier = models.CharField(max_length=255)
    processingbaseline = models.CharField(max_length=255)
    id = models.CharField(max_length=255, primary_key=True)
    instrumentname = models.CharField(max_length=255)
    ondemand = models.BooleanField()
    summary = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    instrumentshortname = models.CharField(max_length=255)
    link_alternative = models.CharField(max_length=255)
    sensoroperationalmode = models.CharField(max_length=255)
    tileid = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    granuleidentifier = models.CharField(max_length=255)
    platformname = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    link_icon = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    datastripidentifier = models.CharField(max_length=255)
    platformserialidentifier = models.CharField(max_length=255)
    ingestiondate = models.CharField(max_length=255)
    processinglevel = models.CharField(max_length=255)
    platformidentifier = models.CharField(max_length=255)
    s2datatakeid = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Propertie"
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.datatakesensingstart
