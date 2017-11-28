from __future__ import unicode_literals

from django.db import models
from django.utils.encoding  import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Associations(models.Model):
    origine = models.CharField(max_length=200)
    type_asso = models.CharField(max_length=200)
    sous_type_asso = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)

    def __str__(self) :
        return self.origine

    def dest(self) :
        return self.destination
