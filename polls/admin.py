from typing import Any, Optional
from tenants.utils import tenant_from_request, set_tenant_schema_for_request
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Poll

# Register your models here.
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    fields = ["question", "tenant", "created_by", "pub_date"]
    readonly_fields = ["pub_date", "updated_at"]

    def formfield_for_foreignkey(self, db_field, request: Optional[HttpRequest], **kwargs: Any):
        #if db_field.name == 'tenant':
        #set_tenant_schema_for_request(request)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request: HttpRequest, *args, **kwargs) -> QuerySet:
        #set_tenant_schema_for_request(request)
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset 
    
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        #set_tenant_schema_for_request(request)
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        return super().save_model(request, obj, form, change)
        

