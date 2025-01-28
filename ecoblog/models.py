from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(_("Categoría"), max_length=50)
    
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name


class ProtectedArea(models.Model):
    name = models.CharField(_("Nombre"), max_length=100)
    category = models.ForeignKey(Category, verbose_name=_("Categoría"), on_delete=models.CASCADE)
    image = models.ImageField(_("Imagen"), upload_to='images/ecoblog')    
    address = models.CharField(_("Dirección"), max_length=200)

    description = HTMLField(_('Descripción'))
    flora = HTMLField(_("Flora"), blank=True, null=True)  
    fauna = HTMLField(_("Fauna"), blank=True, null=True)
    activities = HTMLField(_("Actividades"), blank=True, null=True)

    established_date = models.DateField(_("Fecha establecido"), blank=True, null=True)

    class Meta:
        verbose_name = _("protectedarea")
        verbose_name_plural = _("protectedareas")

    def __str__(self):
        return self.name

