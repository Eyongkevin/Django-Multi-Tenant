from django.contrib import admin
from .models import Tenant
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from typing import Any
from django.utils.translation import ugettext_lazy as _


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    fields = ['name', 'age', 'gender', 'subdomain_prefix']

    def get_queryset(self, request: HttpRequest) -> QuerySet:

        return super().get_queryset(request)

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:

        return super().save_model(request, obj, form, change)
