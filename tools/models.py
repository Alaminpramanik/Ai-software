from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel

class EmailExtract(models.Model):
    email = models.CharField(max_length=300, verbose_name=_('email'),null=True,blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['email', ]),
        ]
    
    def __str__(self):
        return 'id - {}, - emails {}'.format(self.id, self.email)
