from django.db import models

# Create your models here.
class Tenant(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICE = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    name = models.CharField( max_length=100)
    age = models.PositiveIntegerField(default=17)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=50, default=MALE)
    subdomain_prefix = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.subdomain_prefix
    

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, default=1)

    class Meta:
        abstract = True