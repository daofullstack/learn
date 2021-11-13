from django.db import models
import jsonfield

# Create your models here.


class SentinelData(models.Model):
    """Model definition for SentinelData."""

    # TODO: Define fields here
    data = jsonfield.JSONField(default={})
    norm_factor = models.FloatField(default=0)
    image = models.FileField(upload_to="sentinel", default="file.png")

    class Meta:
        """Meta definition for SentinelData."""

        verbose_name = "SentinelData"
        verbose_name_plural = "SentinelDatas"

    def __str__(self):
        """Unicode representation of SentinelData."""
        pass
