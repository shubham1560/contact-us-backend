from django.db import models
from django.contrib.auth.models import AbstractUser
from domain.models import Domain
from django.db import models
from .business_rules import after_insert, before_insert
# Create your models here.


class SysUser(AbstractUser):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null=True, blank=True)
    domain_path = models.CharField(max_length=256, default='/')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        before_insert(self)
        super().save(*args, **kwargs)
        after_insert(self)

    def delete(self, using=None, keep_parents=False):
        super(Domain, self).delete()
