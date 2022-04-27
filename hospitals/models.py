from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(_("Hospital Name"), max_length=200)
    lon = models.FloatField(_("Longitude"))
    lat = models.FloatField(_("Latitude"))
    fid = models.IntegerField(_("Field ID"))
    beds = models.IntegerField(_("Bed Numbers"), default=1)
    province_name = models.CharField(_("Province"), max_length=100)
    province_code = models.CharField(_("Province Code"), max_length=100)

    geom = models.PointField(srid=4326)

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
