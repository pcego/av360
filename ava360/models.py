from django.db import models


class Departament(models.Model):
    description = models.CharField(max_length=100)
    phone = models.CharField(max_length=5)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.description + ' Phone: ' + self.phone