from django.db import models

# Create your models here.
class Tenant(models.Model):
    name = models.CharField( max_length=100)
    age = models.PositiveIntegerField(default=18)
    subdomain_prefix = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.subdomain_prefix
    

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, default=1)

    class Meta:
        abstract = True