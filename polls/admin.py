from typing import Any
from tenants.utils import tenant_from_request
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Poll

# Register your models here.
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    fields = ["question", "tenant", "created_by", "pub_date"]
    readonly_fields = ["pub_date"]

    def get_queryset(self, request: HttpRequest, *args, **kwargs) -> QuerySet:
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset 
    
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        return super().save_model(request, obj, form, change)
        

