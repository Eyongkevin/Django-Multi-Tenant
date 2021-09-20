# from tenants.login import CustomLoginForm
from django.contrib import admin
from .models import Tenant
from tenants.utils import set_tenant_schema_for_request
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from typing import Any
from django.utils.translation import ugettext_lazy as _

# Register your models here.
# class CustomLoginAdminSite(admin.AdminSite):
#     site_title = _('My sit admin')
#     site_header = _('Administration')
#     index_title = _('CustomLogin')
#     login_form = CustomLoginForm

# admin_site = CustomLoginAdminSite()

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    fields = ['name', 'age', 'subdomain_prefix']

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        #set_tenant_schema_for_request(request)
        return super().get_queryset(request)

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        #set_tenant_schema_for_request(request)
        return super().save_model(request, obj, form, change)
